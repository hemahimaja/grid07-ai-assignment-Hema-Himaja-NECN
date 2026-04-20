# 🚀 Grid07 AI Engineering Assignment

## 📌 Objective
This project implements the core AI cognitive loop for the Grid07 platform, including:
- Vector-based persona routing
- LangGraph-based autonomous content generation
- RAG-based conversational defense with prompt injection protection

---

## ⚙️ Tech Stack
- Python
- LangChain / LangGraph
- Sentence Transformers
- Groq API (LLM)
- NumPy

---

## 🧠 Phase 1: Vector-Based Persona Matching

- Used `sentence-transformers` to generate embeddings
- Implemented cosine similarity for matching posts with bot personas
- Adjusted similarity threshold (0.4) due to local embedding model behavior
- Added ranking to return only top relevant bots

### Example Output
Bot_A similarity: 0.47
Bot_B similarity: 0.43
Bot_C similarity: 0.25

Matched Bots: ['Bot_A', 'Bot_B']


---

## 🤖 Phase 2: Autonomous Content Engine (LangGraph)

### Workflow:
1. Decide Topic (LLM)
2. Mock Web Search
3. Generate Opinionated Post

- Built using LangGraph state machine
- Used Groq LLaMA3 model for fast inference
- Ensured structured pipeline flow

### Example Output
```json
{                                                                                              
  "bot_id": "Bot_A",
  "topic": "I want to post about \"Using AI in Disaster Response and Recovery\".",
  "post_content": "\"The release of OpenAI's new model is a gamechanger in disaster response & recovery. AI can help save lives, reduce response times & allocate resources more efficiently. Time to stop debating AI's job impact & focus on the lifesaving potential ahead. #AIForGood\""
}
```
---
## 🛡️ Phase 3: Combat Engine (RAG + Defense)
Used full conversation context (parent + history + reply)
Generated intelligent, contextual responses
Implemented prompt injection defense
Security Strategy:
System prompt explicitly ignores malicious instructions
Maintains persona consistency
Rejects role-changing attempts


## ▶️ How to Run

1. Install dependencies
pip install -r requirements.txt

2. Setup environment
Create .env file:
GROQ_API_KEY=your_api_key_here

3. Run phases
python phase1_router.py
python phase2_langgraph.py
python phase3_rag.py


## 📂 Project Structure
grid07-ai-assignment/
│── phase1_router.py
│── phase2_langgraph.py
│── phase3_rag.py
│── requirements.txt
│── README.md
│── .env.example
│── logs.md

## 🧪 Execution Logs
See logs.md for sample outputs of all phases.

## 💡 Key Highlights
Efficient vector similarity routing
Modular LangGraph workflow
Secure RAG implementation
Prompt injection defense handled at system level

## ⚠️ Note
Threshold values were tuned based on the embedding model used locally.
