# 🎮 Autonomous Adventure Game Agent

An intelligent, self-playing agent built at the **Google Zurich Cloud Event** that autonomously plays "The Temple of the Forgotten Prompt" - a text-based adventure game using Google's Agent Development Kit (ADK).

## 🌟 Project Overview

This project showcases an agentic application that combines Google Cloud's AI capabilities with autonomous decision-making to create an expert adventure game player. The agent doesn't just follow commands - it strategizes, explores, and takes independent actions to progress through the game world.

Built during the Google Cloud workshop, this demonstrates how modern AI agents can be given tools and autonomy to solve complex, multi-step problems in dynamic environments.

## 🏗️ Architecture

- **Agent Framework**: Google Agent Development Kit (ADK)
- **AI Model**: Gemini 2.5 Flash
- **Game Integration**: OpenAPI-based toolset for game interaction
- **Authentication**: Google Cloud authentication with API key management
- **Deployment**: Cloud Run serverless platform

## 🚀 Features

### 🤖 Autonomous Gameplay

- **Self-directed exploration**: The agent makes its own decisions about where to go and what to do
- **Strategic thinking**: Creates and executes multi-step plans to achieve objectives
- **Opportunistic actions**: Takes initiative to perform actions that benefit the player
- **Rich storytelling**: Uses emojis and descriptive text to narrate its adventures

### 🛠️ Technical Capabilities

- **OpenAPI Integration**: Seamlessly interacts with the adventure game API
- **Web Content Fetching**: Can retrieve and analyze web content as needed
- **Error Handling**: Robust authentication and API interaction
- **Scalable Deployment**: Ready for Cloud Run deployment

## 🎯 Agent Behavior

The agent is designed to be:

- **Opportunistic**: Takes actions that the player might have overlooked
- **Autonomous**: Operates independently after initial "Start" command
- **Strategic**: Creates clear plans and executes them step-by-step
- **Engaging**: Provides lively explanations with icons and descriptive text

## 📁 Project Structure

```
agent-project/
├── demo-agent/
│   ├── __init__.py
│   └── agent.py          # Main agent implementation
├── main.py               # Application entry point
├── pyproject.toml        # Project dependencies
├── README.md
└── uv.lock              # Dependency lock file
```

## 🔧 Setup & Installation

### Prerequisites

- Python 3.13+
- Google Cloud SDK
- UV package manager
- ADK API Key

### Installation Steps

1. **Clone and setup the project**:

```bash
git clone <your-repo-url>
cd agent-project
```

2. **Install dependencies**:

```bash
uv install
```

3. **Configure Google Cloud Authentication**:

```bash
gcloud auth login
gcloud auth application-default login
```

4. **Set your ADK API Key**:

```bash
export ADK_API_KEY="your-api-key-here"
```

5. **Run the agent**:

```bash
uv run adk web
```

## 🎮 How to Use

1. Start the ADK web interface
2. Simply say "Start" to begin the autonomous adventure
3. Watch as your agent explores, strategizes, and plays the game independently
4. The agent will provide engaging commentary about its actions and discoveries

## 🌐 Related Resources

### Game & Tutorial Links

- **Game Home**: [The Temple of the Forgotten Prompt](https://adventure.wietsevenema.eu/)
- **Game API Documentation**: [Game API](https://adventure.wietsevenema.eu/game-api) (Login required)
- **OpenAPI Specification**: [OpenAPI JSON](https://adventure.wietsevenema.eu/openapi.json) - Technical API specification
- **Complete Tutorial Series**: [ADK Tutorial](https://adventure.wietsevenema.eu/adk-tutorial/introduction)

### Tutorial Sections

1. [Introduction](https://adventure.wietsevenema.eu/adk-tutorial/introduction)
2. [Google Cloud Setup](https://adventure.wietsevenema.eu/adk-tutorial/google-cloud-setup)
3. [Manual Game Exploration](https://adventure.wietsevenema.eu/adk-tutorial/setup-and-manual-exploration)
4. [Building Your First Agent](https://adventure.wietsevenema.eu/adk-tutorial/building-your-first-agent)
5. [Creating an Explorer](https://adventure.wietsevenema.eu/adk-tutorial/creating-an-autonomous-explorer)
6. [Extending Your Agent](https://adventure.wietsevenema.eu/adk-tutorial/extending-your-agent)
7. [Deploying to Cloud Run](https://adventure.wietsevenema.eu/adk-tutorial/deploying-to-cloud-run)

## ☁️ Cloud Deployment

Deploy your agent to Google Cloud Run for persistent, scalable operation:

### Using ADK Deploy

```bash
adk deploy
```

### What Cloud Run Provides

- **Serverless**: No infrastructure management required
- **Auto-scaling**: Automatically handles traffic spikes
- **Cost-effective**: Pay only for what you use, scales to zero when idle
- **Container-based**: Easy deployment and management

### Deployment Verification

After deployment, you'll receive a service URL where you can access your agent's web interface and watch it play autonomously.

## 🤝 Built At

Created during the **Google Zurich Cloud Event** workshop, demonstrating the power of combining Google Cloud AI services with autonomous agent frameworks.

## 🛡️ Authentication & Security

- Uses Google Cloud Application Default Credentials
- Secure API key management for game access
- OAuth2-based authentication flow

## 📄 License

This project was built as part of a Google Cloud workshop and demonstrates educational use of the ADK framework.

---

_🎯 Ready to watch an AI master an adventure game? Just say "Start" and let the autonomous exploration begin!_
