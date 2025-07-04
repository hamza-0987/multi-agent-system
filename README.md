# Multi-Agent System with AutoGen Studio, Groq LLM, and MCP Integration

A sophisticated multi-agent system built with AutoGen Studio AG2, powered by Groq's fast LLM inference, and enhanced with Model Context Protocol (MCP) for external tool integration.

## 🚀 Features

- **AutoGen Studio AG2**: Latest multi-agent framework with web UI
- **Groq LLM Integration**: Fast inference with Llama3, Mixtral, and Gemma2 models
- **MCP Connectivity**: External tool integration via Model Context Protocol
- **Multiple Agent Teams**: Research and Development specialized teams
- **Interactive Interface**: Both CLI and web-based interfaces
- **Tool Integration**: File operations, web search, GitHub integration
- **Conversation History**: Persistent conversation storage

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js and npm (for MCP servers)
- Groq API key ([Get one here](https://console.groq.com/keys))
- UV package manager (used for dependency management)

## 🛠️ Installation

1. **Navigate to the project directory:**
   ```bash
   cd "D:\python projects\local ai agent ollama openai\local_ai_agent\multi-agent-system"
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure environment:**
   - Edit the `.env` file
   - Replace `your_groq_api_key_here` with your actual Groq API key

4. **Optional: Install Node.js dependencies for MCP servers:**
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   npm install -g @modelcontextprotocol/server-github
   ```

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Groq API Configuration
GROQ_API_KEY=your_actual_groq_api_key

# AutoGen Studio Configuration
AUTOGEN_STUDIO_PORT=8081
AUTOGEN_STUDIO_HOST=localhost

# MCP Configuration
MCP_ENABLED=true
MCP_SERVERS_CONFIG_PATH=./mcp_servers.json

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=autogen_studio.log
```

## 🚀 Getting Started

### Quick Start

Run the startup script:
```bash
uv run python start_system.py
```

This will:
1. Check your environment configuration
2. Verify dependencies
3. Present options to start the system

### Manual Start Options

#### 1. Multi-Agent System (CLI)
```bash
uv run python multi_agent_system.py
```

#### 2. AutoGen Studio (Web Interface)
```bash
uv run autogenstudio ui --host localhost --port 8081
```

## 🤖 Agent Teams

### Research Team
- **Researcher**: Conducts thorough research and information gathering
- **Analyst**: Analyzes data and provides insights
- **TechnicalExpert**: Provides technical expertise and solutions
- **Coordinator**: Manages workflows and synthesizes results

### Development Team
- **Developer**: Writes and reviews code
- **Architect**: Designs system architecture
- **Tester**: Creates tests and ensures quality
- **DevOps**: Manages deployment and infrastructure

## 🔧 Available Tools

The system provides several built-in tools through MCP integration:

- `read_file(file_path)`: Read file contents from workspace
- `write_file(file_path, content)`: Write content to files
- `list_files(directory)`: List files in directories
- `web_search(query)`: Search the web for information
- `github_search(query)`: Search GitHub repositories

## 💬 Usage Examples

### Example 1: Research Task

```python
research_task = """
I need comprehensive research on the current state of AI multi-agent systems. Please:

1. Research the latest developments in multi-agent AI systems
2. Analyze the key technologies and frameworks being used
3. Identify current challenges and limitations
4. Provide technical insights on implementation approaches
5. Create a structured report with findings and recommendations

Please work collaboratively to provide a thorough analysis.
"""
```

### Example 2: Development Task

```python
development_task = """
I need to develop a distributed task management system. Please:

1. Design the system architecture for a distributed task manager
2. Implement core components and APIs
3. Create comprehensive test cases
4. Set up deployment and monitoring infrastructure
5. Document the entire system

Please work together to deliver a complete solution.
"""
```

## 📁 Project Structure

```
multi-agent-system/
├── README.md                    # This file
├── pyproject.toml              # Project dependencies
├── .env                        # Environment configuration
├── mcp_servers.json            # MCP server configurations
├── multi_agent_system.py       # Main multi-agent system
├── start_system.py             # Startup script
├── workspace/                  # Agent workspace directory
├── conversation_history.json   # Saved conversations
└── autogen_studio.log         # System logs
```

## 🛠️ Troubleshooting

### Common Issues

1. **Groq API Key Not Found**
   - Ensure `.env` file has the correct API key
   - Verify the key is active on Groq Console

2. **MCP Servers Not Working**
   - Install Node.js and npm
   - Install required MCP server packages
   - Check `mcp_servers.json` configuration

3. **Import Errors**
   - Run `uv sync` to install dependencies
   - Ensure you're using the project's virtual environment

4. **Port Already in Use**
   - Change the port in `.env` file
   - Kill existing processes using the port

### Debug Mode

Enable debug logging by setting in `.env`:
```env
LOG_LEVEL=DEBUG
```

## 🎯 Groq Models Available

The system supports various Groq models:

- `llama3-8b-8192`: Fast and efficient for most tasks
- `llama3-70b-8192`: More capable for complex reasoning
- `mixtral-8x7b-32768`: Good balance of speed and capability
- `gemma2-9b-it`: Optimized for instruction following

Change the model in `multi_agent_system.py`:
```python
groq_config = GroqModelClient(model="llama3-70b-8192")
```

## 🌐 Web Interface (AutoGen Studio)

Access the web interface at: `http://localhost:8081`

Features:
- Visual agent configuration
- Real-time conversation monitoring
- Team management interface
- Tool integration dashboard

## 🔗 Links

- [AutoGen Studio Documentation](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/)
- [Groq API Documentation](https://console.groq.com/docs)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [UV Package Manager](https://docs.astral.sh/uv/)

---

**Happy Multi-Agent Computing!** 🤖✨
