#!/usr/bin/env python3
"""
Simple Multi-Agent Demo with MCP Integration
"""

import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

async def demonstrate_mcp_agents():
    """Demonstrate multi-agent system with MCP tools"""
    print("🤖 Multi-Agent System with MCP Integration Demo")
    print("=" * 60)
    
    try:
        # Import the system
        sys.path.append('.')
        from multi_agent_system import MultiAgentSystem
        
        # Initialize system
        system = MultiAgentSystem()
        print("✅ Multi-Agent System initialized with MCP integration")
        
        # Show available tools
        tools = system.get_available_tools()
        print(f"\n🔧 Available MCP Tools ({len(tools)}):")
        for i, tool in enumerate(tools, 1):
            print(f"   {i}. {tool}")
        
        # Show MCP servers
        servers = system.get_mcp_servers()
        print(f"\n📡 MCP Servers ({len(servers)}):")
        for name, config in servers.items():
            print(f"   - {name}: {config.get('description', 'No description')}")
        
        # Demo file operations
        print(f"\n📁 Demonstrating File Operations...")
        
        # Get MCP functions
        mcp_integration = system.mcp_integration
        functions = mcp_integration.create_tool_functions()
        
        # Create a demo task file
        task_content = """# Multi-Agent Task Demo

## Task: Develop a Python web scraper

### Requirements:
1. Extract data from websites
2. Store data in CSV format
3. Handle rate limiting
4. Add error handling

### Team Assignment:
- Developer: Implement scraper logic
- Architect: Design system architecture  
- Tester: Create test cases
- DevOps: Setup deployment pipeline

### Status: Ready for team collaboration
"""
        
        write_result = functions['write_file']('demo_task.md', task_content)
        print(f"✅ {write_result}")
        
        # List workspace files
        files_result = functions['list_files']('.')
        print(f"✅ {files_result}")
        
        # Read the file back
        content = functions['read_file']('demo_task.md')
        print(f"✅ Read demo_task.md: {len(content)} characters")
        
        # Setup teams
        print(f"\n👥 Setting up Agent Teams...")
        
        # Research team
        research_team = system.setup_research_team()
        print(f"✅ Research Team: {len(system.agents)} agents")
        for agent_name, agent in system.agents.items():
            print(f"   - {agent.name} ({agent_name})")
        
        # Development team  
        dev_team = system.setup_development_team()
        print(f"✅ Development Team: {len(system.agents)} agents")
        for agent_name, agent in system.agents.items():
            print(f"   - {agent.name} ({agent_name})")
        
        # Demo task simulation
        print(f"\n🎯 Task Simulation...")
        
        sample_tasks = [
            {
                "type": "research",
                "title": "AI Multi-Agent Research",
                "description": "Research current trends in AI multi-agent systems"
            },
            {
                "type": "development", 
                "title": "Web Scraper Development",
                "description": "Develop a robust web scraping system"
            }
        ]
        
        for task in sample_tasks:
            print(f"\n📋 {task['title']} ({task['type']} team)")
            print(f"   Description: {task['description']}")
            
            # Simulate team setup
            if task['type'] == 'research':
                team = system.setup_research_team()
            else:
                team = system.setup_development_team()
            
            print(f"   ✅ Team ready: {len(system.agents)} agents with {len(tools)} MCP tools")
            
            # Create task file
            task_file = f"{task['type']}_task.md"
            task_content = f"# {task['title']}\n\n{task['description']}\n\n## Team: {task['type'].title()}\n## Status: Ready for collaboration\n## Tools: {', '.join(tools)}"
            
            write_result = functions['write_file'](task_file, task_content)
            print(f"   ✅ {write_result}")
        
        print(f"\n🎉 Demo Complete!")
        print(f"✅ MCP integration working perfectly")
        print(f"✅ File operations functional") 
        print(f"✅ Multi-agent teams ready")
        print(f"✅ External tools accessible")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def interactive_demo():
    """Interactive demo menu"""
    print("\n" + "=" * 60)
    print("🎮 Interactive Multi-Agent Demo")
    print("=" * 60)
    
    while True:
        print("\n🎯 Options:")
        print("1. Run MCP Integration Demo")
        print("2. Test File Operations")
        print("3. Show Agent Teams")
        print("4. Create Custom Task")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            await demonstrate_mcp_agents()
            
        elif choice == "2":
            print("\n📁 Testing File Operations...")
            sys.path.append('.')
            from multi_agent_system import MCPIntegration
            
            mcp = MCPIntegration()
            functions = mcp.create_tool_functions()
            
            # Test operations
            test_content = f"# Test File\n\nCreated at: {asyncio.get_event_loop().time()}\n\nMCP Integration: Working ✅"
            result = functions['write_file']('test_interactive.md', test_content)
            print(f"✅ {result}")
            
            content = functions['read_file']('test_interactive.md')
            print(f"✅ Read file content:\n{content}")
            
            files = functions['list_files']('.')
            print(f"✅ {files}")
            
        elif choice == "3":
            print("\n👥 Agent Teams Overview...")
            sys.path.append('.')
            from multi_agent_system import MultiAgentSystem
            
            system = MultiAgentSystem()
            
            print("\n🔬 Research Team:")
            research_team = system.setup_research_team()
            for agent_name, agent in system.agents.items():
                print(f"   - {agent.name}: {agent_name}")
            
            print("\n💻 Development Team:")
            dev_team = system.setup_development_team()
            for agent_name, agent in system.agents.items():
                print(f"   - {agent.name}: {agent_name}")
                
        elif choice == "4":
            print("\n📝 Create Custom Task...")
            task_title = input("Task title: ").strip()
            task_desc = input("Task description: ").strip()
            team_type = input("Team type (research/development): ").strip().lower()
            
            if task_title and task_desc and team_type in ['research', 'development']:
                sys.path.append('.')
                from multi_agent_system import MultiAgentSystem
                
                system = MultiAgentSystem()
                functions = system.mcp_integration.create_tool_functions()
                
                # Create task file
                task_content = f"# {task_title}\n\n## Description\n{task_desc}\n\n## Team Type\n{team_type.title()}\n\n## Status\nReady for team collaboration\n\n## Available Tools\n"
                for tool in system.get_available_tools():
                    task_content += f"- {tool}\n"
                
                filename = f"custom_{team_type}_task.md"
                result = functions['write_file'](filename, task_content)
                print(f"✅ {result}")
                
                # Setup appropriate team
                if team_type == 'research':
                    team = system.setup_research_team()
                else:
                    team = system.setup_development_team()
                
                print(f"✅ {team_type.title()} team ready with {len(system.agents)} agents")
            else:
                print("❌ Invalid input. Please try again.")
                
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please select 1-5.")

async def main():
    """Main function"""
    print("🚀 Starting Multi-Agent System Demo...")
    
    # Run initial demo
    success = await demonstrate_mcp_agents()
    
    if success:
        # Run interactive demo
        await interactive_demo()
    else:
        print("❌ Demo failed. Check your configuration.")

if __name__ == "__main__":
    asyncio.run(main())
