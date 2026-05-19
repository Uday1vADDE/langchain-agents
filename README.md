# LangChain Basics & AI Agent 🤖

A hands-on exploration of LangChain framework — from basics to 
building a working AI agent with multiple tools.

---

## What's Inside

### 1. `langchain_basics.py` — LangChain Fundamentals
Learning LangChain's core concepts — standard LLM interface, 
prompt templates and chains.

### 2. `agent.py` — AI Agent with Tools
A working AI agent that autonomously decides which tool to use 
based on your question.

---

## Why LangChain?

Every LLM provider has different syntax:
- Groq → `response.choices[0].message.content`
- Gemini → `response.text`
- OpenAI → `response.choices[0].message.content`

LangChain wraps all providers in one standard interface:
```python
# Groq
llm = ChatGroq(model="...", api_key="...")
answer = llm.invoke("question").content

# Switch to OpenAI — just change ONE line
llm = ChatOpenAI(model="...", api_key="...")
answer = llm.invoke("question").content
```

Same code. Different provider. Just change the first line.

---

## Key Concepts Learned

**Prompt Templates — Fill in the blank:**
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in simple words.")
])
chain.invoke({"topic": "RAG"})
chain.invoke({"topic": "embeddings"})
```

**Chains — Connect steps with `|`:**
```python
chain = prompt | llm
response = chain.invoke({"topic": "AI agents"})
```

**Custom Tools with `@tool` decorator:**
```python
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression like '2+2' or '10*5'"""
    return str(eval(expression))
```
The docstring is critical — LLM reads it to decide WHEN to use the tool.

**ReAct Pattern — How agent thinks:**
Thought → "I need to search for this"
Action  → uses DuckDuckGo search tool
Observation → reads search results
Thought → "I have enough info now"
Action  → gives final answer
---

## Agent Tools

| Tool | Purpose | When Agent Uses It |
|---|---|---|
| DuckDuckGoSearch | Search the internet | Current events, facts, news |
| Calculator | Math calculations | Any arithmetic expression |

---

## How it Works

You give a goal
↓
Agent (LLM brain) reads your question
↓
Checks available tools and their descriptions
↓
Picks the right tool automatically
↓
Runs tool → reads result
↓
Decides if more searching needed
↓
Forms final answer

---

## Tech Stack
- **LangChain** — AI framework and standard interface
- **Groq (Llama 3.1)** — LLM brain of the agent
- **DuckDuckGo** — free web search tool
- **LangGraph** — agent execution framework
- **python-dotenv** — secure API key management

---

## Run Locally

**Step 1 — Clone the repo**
```bash
git clone https://github.com/Uday1vADDE/langchain-agents.git
cd langchain-agents
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Create .env file**

GROQ_API_KEY=your-groq-api-key-here

**Step 4 — Run LangChain basics**
```bash
python langchain_basics.py
```

**Step 5 — Run the agent**
```bash
python agent.py
```

---

## What I Learned
- Why LangChain exists and what problem it solves
- How prompt templates make code reusable
- How chains connect multiple steps cleanly
- How agents autonomously decide which tool to use
- Why tool docstrings matter — LLM reads them to pick tools
- The ReAct pattern — how agents think and act in loops
- Limitations of current agents — multi-part questions, fake sources
