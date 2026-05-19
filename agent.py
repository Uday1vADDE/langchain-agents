from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.tools import tool
import os

load_dotenv()

# Step 1 — LLM (the brain)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# Step 2 — Tools
search = DuckDuckGoSearchRun()

#calculator  (custom tool)
@tool
def calculator(expression: str) -> str:
    """"Calculate a mathematical expression. Input should be a math expression like 
     '2+2' or '10*5' """
    
    try:
        result=eval(expression)
        return str(result)
    except:
        return "invalid expression"


tools = [search,calculator]

# Step 3 — Create agent
agent = create_agent(llm, tools)

print("Agent ready!")
print(f"Tools available: {[tool.name for tool in tools]}")

response=agent.invoke(
    {
        "messages":[("human","Who is persent ceo of google ?")]
    }
)

print(response["messages"][-1].content)

for message in response["messages"]:
    print(f'\nType:{type(message).__name__}')
    print(f'Content:{message.content}')
    print("----")