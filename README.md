# iPop Support Agent

An AI-powered **customer support agent** branded as **iPop**  
Built with **LiveKit**, **Cartesia (Voice)**, **Deepgram (Speech-to-Text)**, **Google Gemini (LLM)**, **Pinecone (Vector DB)**, and a **React frontend**.  
It provides real-time conversational assistance, knowledge base search, and a modern UI.

---

## Features
- Branded as **iPop Support Agent** – friendly, reliable customer assistant.
- Real-time AI agent powered by [LiveKit Agents](https://docs.livekit.io/agents/).
- Natural, human-like **voice responses** with [Cartesia](https://cartesia.ai/).
- Accurate **speech recognition** via [Deepgram](https://deepgram.com/).
- Smart reasoning with [Google Gemini](https://deepmind.google/technologies/gemini/).
- Knowledge base search using [Pinecone](https://www.pinecone.io/).
- React frontend (`agent-starter-react`) for user interaction.
- Console + Dev modes for testing.

---

## Project Structure
```
Customer-Support-Agent/
│── agent.py # Main Python agent runner
│── .env # Environment variables (create your own)
│── .gitignore
│── agent-starter-react/ # Next.js + React frontend (UI shows "iPop Support")

```
---

## Setup

### 1️ Clone the repo
```bash
git clone https://github.com/prashantpq/Customer-Support-Agent.git
cd Customer-Support-Agent
```

### 2 Python Environment
```bash
conda create -n customer python=3.11 -y
conda activate customer
```

### 3 Environement Variables
```bash
# LiveKit API (realtime agent infra)
LIVEKIT_URL=https://your-livekit-server-url
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret

# Pinecone (knowledge base)
PINECONE_API_KEY=your_pinecone_key

# Cartesia (voice generation)
CARTESIA_API_KEY=your_cartesia_key

# Deepgram (speech recognition)
DEEPGRAM_API_KEY=your_deepgram_key

# Google Gemini (LLM reasoning)
GEMINI_API_KEY=your_gemini_key

```

### 4 Run Agent
Console Mode
```bash
python3 agent.py console
```

Dev Mode
```bash
python3 agent.py dev
```

### Run Frontend
```bash
cd agent-starter-react
pnpm install
pnpm dev
```
Frontend will be available at -> http://localhost:3000.
Here you’ll see the branded iPop Support UI. 