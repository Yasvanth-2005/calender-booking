import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.agents import tool, initialize_agent, AgentType

from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  


llm = ChatGroq(
    streaming=False,
    api_key=GROQ_API_KEY,
    model="llama3-8b-8192"  
)


@tool
def add_calendar_event(event: str) -> str:
    """Add an event to the calendar. The input should contain both the description and the date (e.g., 'dentist appointment on 2024-08-24'). Returns confirmation."""
    import re
    match = re.search(r"(.+) on (\d{4}-\d{2}-\d{2})", event)
    if match:
        description, date = match.group(1), match.group(2)
        return f"Event '{description.strip()}' added to your calendar on {date}."
    return "Could not parse event description and date. Please use the format: '<description> on YYYY-MM-DD'."

tools = [add_calendar_event]

system_prompt = (
    "You are a helpful assistant that can use tools to answer questions. "
    "If the user asks to add an event to their calendar, extract the event description and date from the conversation. "
    "If the user confirms (e.g., says 'yes'), use the add_calendar_event tool with the event description and date in the format: '<description> on YYYY-MM-DD'. "
    "Do not use any other tools for confirmations or unrelated tasks. "
    "If the date is not in YYYY-MM-DD format, ask the user to clarify."
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])


agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True
)


def run_agent(message, chat_history=None):
    if chat_history is None:
        chat_history = []
    try:
        print("Input to agent:", message)
        response = agent_executor.invoke({"input": message, "chat_history": chat_history})
        print("Raw response:", response)
        return response.get("output", "⚠️ No output from agent")
    except Exception as e:
        import traceback
        traceback.print_exc()
        error_message = str(e)
        if "Failed to call a function" in error_message:
            return "⚠️ Sorry, this action can't be performed with the current model."
        return f"⚠️ Agent Error: {error_message}"

