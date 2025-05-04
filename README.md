# Basic Research Agent

A Python-based research assistant that leverages Large Language Models (LLMs) and various search tools to perform automated research tasks. The agent can search multiple sources, compile information, and save research results to a file.

## Features

- Uses multiple LLMs (GPT-4 and Claude-3) for processing
- Integrates with Wikipedia and DuckDuckGo for search capabilities
- Automatically saves research results to a text file
- Structured output format using Pydantic models
- Easy to extend with additional tools

## Prerequisites

- Python 3.x
- Virtual environment (recommended)
- API keys for:
  - OpenAI (GPT-4)
  - Anthropic (Claude)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd basic_agent
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Usage

Run the main script to start the research assistant:

```bash
python main.py
```

The agent will prompt you with "What can I help you search?" Enter your research query, and the agent will:
1. Search through multiple sources (Wikipedia, DuckDuckGo)
2. Compile the information
3. Generate a structured response
4. Save the research results to `research.txt`

## Project Structure

- `agent/` - Contains the main agent implementation
- `agent_tools/` - Individual tool implementations (Wikipedia, DuckDuckGo, Save to file)
- `dto/` - Data transfer objects and response models
- `main.py` - Entry point of the application
- `requirements.txt` - Project dependencies

## License

This project is licensed under CC0 1.0 Universal - see the [LICENSE](LICENSE) file for details.