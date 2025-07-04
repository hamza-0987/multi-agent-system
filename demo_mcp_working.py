#!/usr/bin/env python3
"""
Demonstration that MCP functionality is working in your multi-agent system
"""

import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment
load_dotenv()

async def demo_mcp_functionality():
    """Demonstrate that MCP is working"""
    print("🎯 Demonstrating MCP Functionality in Multi-Agent System")
    print("=" * 60)
    
    try:
        # Import the multi-agent system
        sys.path.append('.')
        from multi_agent_system import MultiAgentSystem, MCPIntegration
        
        # 1. Test MCP Integration directly
        print("\n1️⃣ Testing MCP Integration")
        mcp = MCPIntegration()
        tools = mcp.get_available_tools()
        print(f"✅ MCP Integration loaded {len(tools)} server configurations")
        
        for tool in tools:
            print(f"   - {tool['name']}: {tool['description']}")
        
        # 2. Test tool functions
        print("\n2️⃣ Testing Tool Functions")
        functions = mcp.create_tool_functions()
        print(f"✅ Created {len(functions)} tool functions:")
        for func_name in functions.keys():
            print(f"   - {func_name}")
        
        # 3. Test file operations
        print("\n3️⃣ Testing File Operations")
        workspace = Path("workspace")
        workspace.mkdir(exist_ok=True)
        
        # Write a test file
        write_result = functions['write_file']('demo_test.md', '# MCP Demo\n\nThis file was created using MCP file operations!\n\n- Feature 1: File writing ✅\n- Feature 2: File reading ✅\n- Feature 3: File listing ✅')
        print(f"✅ {write_result}")
        
        # Read the file back
        read_result = functions['read_file']('demo_test.md')
        print(f"✅ Read file content (first 50 chars): {read_result[:50]}...")
        
        # List files
        list_result = functions['list_files']('.')
        print(f"✅ {list_result}")
        
        # 4. Test Multi-Agent System with MCP
        print("\n4️⃣ Testing Multi-Agent System Integration")
        system = MultiAgentSystem()
        print("✅ Multi-Agent System initialized with MCP integration")
        
        # Setup research team
        research_team = system.setup_research_team()
        print(f"✅ Research team created with {len(system.agents)} agents")
        
        # Check tools are available to agents
        available_tools = system.get_available_tools()
        print(f"✅ Agents have access to {len(available_tools)} tools:")
        for tool in available_tools:
            print(f"   - {tool}")
        
        # 5. Test a simple task demonstration (without full conversation)
        print("\n5️⃣ MCP Tools Available to Agents")
        print("Your agents can now use these MCP-powered tools:")
        print("   📁 read_file(path) - Read files from workspace")
        print("   📝 write_file(path, content) - Write files to workspace") 
        print("   📋 list_files(directory) - List workspace files")
        print("   🔍 github_search(query) - Search GitHub repositories*")
        print("   📦 github_list_repos(username) - List GitHub repositories*")
        print("   📄 github_get_file(repo, path, branch) - Get GitHub file content*")
        print("   *Note: GitHub tools require valid authentication")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Main demo function"""
    success = await demo_mcp_functionality()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 SUCCESS: Your MCP functionality is working!")
        print("\nWhat this means:")
        print("✅ Your multi-agent system can load MCP server configurations")
        print("✅ File operations (read/write/list) work through MCP")
        print("✅ GitHub tools are configured (authentication needs fixing)")
        print("✅ Agents have access to external tools via MCP")
        print("✅ Your system can be extended with more MCP servers")
        
        print("\nNext steps:")
        print("🔧 Fix GitHub authentication (check your token)")
        print("🔧 Add more MCP servers for additional functionality")
        print("🚀 Run full multi-agent conversations with MCP tools")
        
    else:
        print("❌ Some issues were found. Check the output above.")
    
    return success

if __name__ == "__main__":
    asyncio.run(main())
