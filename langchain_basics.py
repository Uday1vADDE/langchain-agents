from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


#Initialize the llm
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

#messages    
#create template with blank {topic}
prompt=ChatPromptTemplate.from_messages([

    ("system","you are a helpful assistent"),
    ("human","explain {topic} in simple words ?")      #using promt template 
    
])

#connecting promt and llm (chain)
chain =prompt | llm

#test
test = prompt.invoke({"topic": "embeddings"})
print(test)
print("---")


#invoke
response=chain.invoke({"topic":"embeddings"})

#answeer
print(response.content)