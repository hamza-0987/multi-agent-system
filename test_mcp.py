#!/usr/bin/env python3
"""
Test script for MCP functionality in the multi-agent system
"""

import os
import json
import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment
load_dotenv()

def test_environment():
    """Test environment configuration"""
    print("🔧 Testing Environment Configuration...")
    
    # Check Groq API key
    groq_key = os.getenv('GROQ_API_KEY')
    if groq_key and groq_key != 'your_groq_api_key_here':
        print("✅ GROQ_API_KEY is configured")
    else:
        print("❌ GROQ_API_KEY is not configured properly")
        return False
    
    # Check MCP configuration
    mcp_enabled = os.getenv('MCP_ENABLED', 'false').lower() == 'true'
    if mcp_enabled:
        print("✅ MCP is enabled")
    else:
        print("⚠️ MCP is disabled")
    
    return True

def test_mcp_configuration():
    """Test MCP server configuration"""
    print("\n📋 Testing MCP Server Configuration...")
    
    config_path = Path("mcp_servers.json")
    if not config_path.exists():
        print("❌ mcp_servers.json not found")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        servers = config.get('servers', {})
        print(f"✅ Found {len(servers)} MCP server configurations:")
        
        for name, server_config in servers.items():
            print(f"  - {name}: {server_config.get('description', 'No description')}")
            print(f"    Command: {server_config.get('command', 'N/A')}")
            print(f"    Args: {server_config.get('args', [])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading MCP configuration: {e}")
        return False

def test_dependencies():
    """Test required dependencies"""
    print("\n📦 Testing Dependencies...")
    
    dependencies = [
        ('autogen_agentchat', 'AutoGen AgentChat'),
        ('autogen_ext', 'AutoGen Extensions'),
        ('groq', 'Groq'),
        ('dotenv', 'Python DotEnv')
    ]
    
    all_ok = True
    for module, name in dependencies:
        try:
            __import__(module)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            all_ok = False
    
    return all_ok

def test_mcp_integration():
    """Test MCP integration functionality"""
    print("\n🔧 Testing MCP Integration...")
    
    try:
        # Import the MCP integration class
        sys.path.append('.')
        from multi_agent_system import MCPIntegration
        
        # Create MCP integration instance
        mcp = MCPIntegration()
        print("✅ MCPIntegration class instantiated successfully")
        
        # Test getting available tools
        tools = mcp.get_available_tools()
        print(f"✅ Found {len(tools)} available tools:")
        for tool in tools:
            print(f"  - {tool['name']}: {tool['description']}")
        
        # Test creating tool functions
        functions = mcp.create_tool_functions()
        print(f"✅ Created {len(functions)} tool functions:")
        for func_name in functions.keys():
            print(f"  - {func_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ MCP integration test failed: {e}")
        return False

def test_github_mcp():
    """Test GitHub MCP functionality"""
    print("\n🐙 Testing GitHub MCP Integration...")
    
    # Test if GitHub MCP server is configured
    config_path = Path("mcp_servers.json")
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        github_config = config.get('servers', {}).get('github')
        if github_config:
            print("✅ GitHub MCP server is configured")
            print(f"  Command: {github_config.get('command')}")
            print(f"  Args: {github_config.get('args')}")
            
            # Check if GitHub token is configured
            github_token = github_config.get('env', {}).get('GITHUB_PERSONAL_ACCESS_TOKEN')
            if github_token and github_token != 'your_github_token_here':
                print("✅ GitHub token is configured")
                
                # Test the actual MCP GitHub functionality using the available tools
                print("\n🧪 Testing GitHub MCP functionality...")
                
                # Since we have access to the MCP tools through the function calls,
                # let's test a simple GitHub search
                return test_github_with_mcp_tools()
            else:
                print("⚠️ GitHub token not configured or using placeholder")
                return True
        else:
            print("❌ GitHub MCP server not found in configuration")
            return False
    else:
        print("❌ MCP configuration file not found")
        return False

def test_github_with_mcp_tools():
    """Test GitHub functionality using the actual MCP tools available"""
    print("🔍 Testing GitHub MCP tools...")
    
    try:
        # Test GitHub search functionality
        print("Testing GitHub search...")
        result = call_mcp_tool("search_repositories", {"query": "python multi-agent", "perPage": 5})
        if result:
            print("✅ GitHub search functionality is working")
            return True
        else:
            print("⚠️ GitHub search returned no results or failed")
            return False
            
    except Exception as e:
        print(f"❌ GitHub MCP test failed: {e}")
        return False

def test_file_operations():
    """Test file operation functionality"""
    print("\n📁 Testing File Operations...")
    
    # Create workspace directory if it doesn't exist
    workspace = Path("workspace")
    workspace.mkdir(exist_ok=True)
    
    try:
        # Test file operations using MCP integration
        sys.path.append('.')
        from multi_agent_system import MCPIntegration
        
        mcp = MCPIntegration()
        functions = mcp.create_tool_functions()
        
        # Test write file
        if 'write_file' in functions:
            write_result = functions['write_file']('test_mcp.txt', 'Hello from MCP test!')
            print(f"✅ Write file test: {write_result}")
        
        # Test read file
        if 'read_file' in functions:
            read_result = functions['read_file']('test_mcp.txt')
            print(f"✅ Read file test: {read_result}")
        
        # Test list files
        if 'list_files' in functions:
            list_result = functions['list_files']('.')
            print(f"✅ List files test: {list_result}")
        
        return True
        
    except Exception as e:
        print(f"❌ File operations test failed: {e}")
        return False

def test_groq_connectivity():
    """Test Groq API connectivity"""
    print("\n🚀 Testing Groq API Connectivity...")
    
    try:
        sys.path.append('.')
        from multi_agent_system import GroqModelClient
        
        # Test creating Groq client
        groq_client = GroqModelClient()
        print("✅ GroqModelClient instantiated successfully")
        
        # Get the client
        client = groq_client.get_client()
        print("✅ Groq client configured successfully")
        print(f"  Model: {groq_client.model}")
        print(f"  Base URL: https://api.groq.com/openai/v1")
        
        return True
        
    except Exception as e:
        print(f"❌ Groq connectivity test failed: {e}")
        return False

async def test_agent_creation():
    """Test agent creation functionality"""
    print("\n🤖 Testing Agent Creation...")
    
    try:
        sys.path.append('.')
        from multi_agent_system import MultiAgentSystem
        
        # Create multi-agent system
        system = MultiAgentSystem()
        print("✅ MultiAgentSystem instantiated successfully")
        
        # Test research team setup
        research_team = system.setup_research_team()
        print(f"✅ Research team created with {len(system.agents)} agents")
        
        # Test development team setup
        dev_team = system.setup_development_team()
        print(f"✅ Development team created with {len(system.agents)} agents")
        
        # Display available tools
        tools = system.get_available_tools()
        print(f"✅ System has {len(tools)} available tools: {', '.join(tools)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Agent creation test failed: {e}")
        return False

async def main():
    """Main test function"""
    print("🧪 Multi-Agent System MCP Functionality Test")
    print("=" * 60)
    
    tests = [
        ("Environment", test_environment),
        ("MCP Configuration", test_mcp_configuration),
        ("Dependencies", test_dependencies),
        ("MCP Integration", test_mcp_integration),
        ("GitHub MCP", test_github_mcp),
        ("File Operations", test_file_operations),
        ("Groq Connectivity", test_groq_connectivity),
        ("Agent Creation", test_agent_creation),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            if asyncio.iscoroutinefunction(test_func):
                result = await test_func()
            else:
                result = test_func()
            results[test_name] = result
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your MCP functionality is working correctly.")
    else:
        print("⚠️ Some tests failed. Check the output above for details.")
        
    return passed == total

if __name__ == "__main__":
    asyncio.run(main())
