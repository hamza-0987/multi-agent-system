#!/usr/bin/env python3
"""
Startup script for the Multi-Agent System
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

def check_environment():
    """Check if the environment is properly configured"""
    load_dotenv()
    
    groq_api_key = os.getenv('GROQ_API_KEY')
    if not groq_api_key or groq_api_key == 'your_groq_api_key_here':
        print("❌ GROQ_API_KEY not found or not configured properly!")
        print("\n📝 Please follow these steps:")
        print("1. Get your Groq API key from: https://console.groq.com/keys")
        print("2. Edit the .env file and replace 'your_groq_api_key_here' with your actual API key")
        print("3. Run this script again")
        return False
    
    print("✅ Environment configured properly!")
    return True

def install_node_dependencies():
    """Install Node.js dependencies for MCP servers"""
    print("\n📦 Installing Node.js dependencies for MCP servers...")
    try:
        # Check if npm is available
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("⚠️ npm not found. MCP servers might not work without Node.js.")
            return False
        
        print("✅ npm is available")
        return True
        
    except FileNotFoundError:
        print("⚠️ Node.js/npm not found. MCP servers might not work without Node.js.")
        return False

def start_autogen_studio():
    """Start AutoGen Studio web interface"""
    print("\n🚀 Starting AutoGen Studio...")
    try:
        port = os.getenv('AUTOGEN_STUDIO_PORT', '8081')
        host = os.getenv('AUTOGEN_STUDIO_HOST', 'localhost')
        
        print(f"🌐 AutoGen Studio will be available at: http://{host}:{port}")
        
        # Start AutoGen Studio
        subprocess.run([
            'uv', 'run', 'autogenstudio', 'ui', 
            '--host', host, 
            '--port', port
        ])
        
    except KeyboardInterrupt:
        print("\n👋 AutoGen Studio stopped by user")
    except Exception as e:
        print(f"❌ Error starting AutoGen Studio: {e}")

def start_multi_agent_system():
    """Start the multi-agent system"""
    print("\n🤖 Starting Multi-Agent System...")
    try:
        subprocess.run(['uv', 'run', 'python', 'multi_agent_system.py'])
    except KeyboardInterrupt:
        print("\n👋 Multi-Agent System stopped by user")
    except Exception as e:
        print(f"❌ Error starting Multi-Agent System: {e}")

def main():
    """Main startup function"""
    print("🔧 Multi-Agent System Startup")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Install Node.js dependencies
    install_node_dependencies()
    
    # Show menu
    while True:
        print("\n🎯 Select startup option:")
        print("1. Start Multi-Agent System (Command Line)")
        print("2. Start AutoGen Studio (Web Interface)")
        print("3. Check System Status")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            start_multi_agent_system()
            
        elif choice == "2":
            start_autogen_studio()
            
        elif choice == "3":
            print("\n📊 System Status:")
            print(f"✅ Working Directory: {Path.cwd()}")
            print(f"✅ Python Environment: {sys.executable}")
            print(f"✅ .env file exists: {Path('.env').exists()}")
            print(f"✅ MCP config exists: {Path('mcp_servers.json').exists()}")
            print(f"✅ Workspace directory exists: {Path('workspace').exists()}")
            
            # Check Python packages
            try:
                import autogenstudio
                print(f"✅ AutoGen Studio: {autogenstudio.__version__}")
            except ImportError:
                print("❌ AutoGen Studio not installed")
            
            try:
                import groq
                print(f"✅ Groq: {groq.__version__}")
            except ImportError:
                print("❌ Groq not installed")
                
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
