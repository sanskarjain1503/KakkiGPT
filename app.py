from agent import get_agent
from langchain_core.messages import SystemMessage, HumanMessage


# agent = get_agent("gemini-2.5-flash")
agent = get_agent("gemini-3.5-flash")


config = {
    "configurable":{
        "thread_id":"test_thread_id",
    }
}


for message_chunk, mettadata in agent.stream(
    {"messages":[HumanMessage(content="Generate a blog about Machine learning")]},
    config=config,
    stream_mode= "messages"):
    
    if message_chunk.content:
        print(message_chunk.content,end=" ", flush=True)