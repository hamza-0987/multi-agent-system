#!/usr/bin/env python3
"""
Create GitHub repository and upload multi-agent system files
"""

import requests
import json
import base64
import os
from pathlib import Path

def get_github_token():
    """Get GitHub token from MCP configuration"""
    config_path = Path("mcp_servers.json")
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config.get('servers', {}).get('github', {}).get('env', {}).get('GITHUB_PERSONAL_ACCESS_TOKEN')
    return None

def create_repository(token, repo_name, description, private=False):
    """Create a new GitHub repository"""
    url = "https://api.github.com/user/repos"
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
    }
    
    data = {
        'name': repo_name,
        'description': description,
        'private': private,
        'auto_init': True,
        'has_issues': True,
        'has_projects': True,
        'has_wiki': True
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        repo_data = response.json()
        print(f"✅ Repository created successfully!")
        print(f"   Name: {repo_data['name']}")
        print(f"   URL: {repo_data['html_url']}")
        print(f"   Clone URL: {repo_data['clone_url']}")
        return repo_data
    else:
        print(f"❌ Failed to create repository: {response.status_code}")
        print(f"   Error: {response.json().get('message', 'Unknown error')}")
        return None

def upload_file_to_repo(token, owner, repo, file_path, content, message, branch="main"):
    """Upload a file to GitHub repository"""
    # Encode content to base64
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
    }
    
    data = {
        'message': message,
        'content': encoded_content,
        'branch': branch
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f"✅ Uploaded {file_path}")
        return True
    else:
        print(f"❌ Failed to upload {file_path}: {response.status_code}")
        if response.status_code != 422:  # File already exists
            print(f"   Error: {response.json().get('message', 'Unknown error')}")
        return False

def upload_multiple_files(token, owner, repo, files_data, branch="main"):
    """Upload multiple files to repository"""
    print(f"\n📤 Uploading {len(files_data)} files to {owner}/{repo}...")
    
    success_count = 0
    for file_info in files_data:
        file_path = file_info['path']
        content = file_info['content']
        message = file_info.get('message', f'Add {file_path}')
        
        if upload_file_to_repo(token, owner, repo, file_path, content, message, branch):
            success_count += 1
    
    print(f"\n📊 Upload Summary: {success_count}/{len(files_data)} files uploaded successfully")
    return success_count == len(files_data)

def read_local_file(file_path):
    """Read local file content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return None

def main():
    """Main function to create repository and upload files"""
    print("🚀 Creating GitHub Repository for Multi-Agent System")
    print("=" * 60)
    
    # Get GitHub token
    token = get_github_token()
    if not token:
        print("❌ GitHub token not found in configuration")
        return
    
    print(f"✅ GitHub token found: {token[:8]}...{token[-4:]}")
    
    # Repository details
    repo_name = "multi-agent-system"
    description = "Multi-Agent System with AutoGen Studio, Groq LLM, and MCP Integration - A sophisticated multi-agent framework with external tool connectivity"
    
    # Create repository
    repo_data = create_repository(token, repo_name, description, private=False)
    if not repo_data:
        return
    
    owner = repo_data['owner']['login']
    
    # Prepare files to upload
    files_to_upload = []
    
    # Core system files
    core_files = [
        'multi_agent_system.py',
        'start_system.py', 
        'main.py',
        'README.md',
        'pyproject.toml',
        'mcp_servers.json',
        '.env'
    ]
    
    # Test and demo files
    demo_files = [
        'test_mcp.py',
        'demo_mcp_working.py',
        'comprehensive_mcp_test.py',
        'simple_agent_demo.py',
        'create_github_repo.py',
        'MCP_TEST_SUMMARY.md'
    ]
    
    all_files = core_files + demo_files
    
    for file_name in all_files:
        if Path(file_name).exists():
            content = read_local_file(file_name)
            if content is not None:
                # Skip .env file for security (upload template instead)
                if file_name == '.env':
                    content = """# Groq API Configuration
GROQ_API_KEY=your_actual_groq_api_key

# AutoGen Studio Configuration
AUTOGEN_STUDIO_PORT=8081
AUTOGEN_STUDIO_HOST=localhost

# MCP Configuration
MCP_ENABLED=true
MCP_SERVERS_CONFIG_PATH=./mcp_servers.json

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=autogen_studio.log"""
                    file_name = '.env.template'
                
                # Update mcp_servers.json to remove actual token
                if file_name == 'mcp_servers.json':
                    config = json.loads(content)
                    if 'servers' in config and 'github' in config['servers']:
                        config['servers']['github']['env']['GITHUB_PERSONAL_ACCESS_TOKEN'] = 'your_github_token_here'
                    content = json.dumps(config, indent=2)
                
                files_to_upload.append({
                    'path': file_name,
                    'content': content,
                    'message': f'Add {file_name}'
                })
        else:
            print(f"⚠️ File not found: {file_name}")
    
    # Add workspace files if they exist
    workspace_dir = Path('workspace')
    if workspace_dir.exists():
        for workspace_file in workspace_dir.glob('**/*'):
            if workspace_file.is_file():
                content = read_local_file(workspace_file)
                if content is not None:
                    relative_path = str(workspace_file).replace('\\', '/')
                    files_to_upload.append({
                        'path': relative_path,
                        'content': content,
                        'message': f'Add workspace file {relative_path}'
                    })
    
    # Upload all files
    if files_to_upload:
        success = upload_multiple_files(token, owner, repo_name, files_to_upload)
        
        if success:
            print(f"\n🎉 Repository created and files uploaded successfully!")
            print(f"🔗 Repository URL: {repo_data['html_url']}")
            print(f"📋 Clone command: git clone {repo_data['clone_url']}")
        else:
            print(f"\n⚠️ Repository created but some files failed to upload")
            print(f"🔗 Repository URL: {repo_data['html_url']}")
    else:
        print("❌ No files to upload")

if __name__ == "__main__":
    main()
