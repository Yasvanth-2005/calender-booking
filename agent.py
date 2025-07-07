import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.agents import tool, create_tool_calling_agent, AgentExecutor

from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-8b-8192"  
)


@tool
def get_current_year() -> str:
    """Returns the current year."""
    from datetime import datetime
    return str(datetime.now().year)

tools = [get_current_year]


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can use tools to answer questions."),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])


agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def run_agent(message: str):
    return agent_executor.invoke({"input": message})["output"]
