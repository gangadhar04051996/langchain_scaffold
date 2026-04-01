from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from data_models.response_models import TemperatureResponseModel
from models_config.get_model_object import get_openai_model
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

import asyncio, uuid
import os


checkpointer = InMemorySaver()

chat_model = get_openai_model("low")
async def main():
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    mcp_client= MultiServerMCPClient(
        {
            "weather_server":{
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            }
        }
    )
    tools = await mcp_client.get_tools()
    agent = create_agent(model=chat_model,
                         tools=tools,
                         checkpointer=checkpointer,
                         response_format=ToolStrategy(TemperatureResponseModel)
                         )
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in Mesa Arizona"}]},
        config = config
    )
    print(response["structured_response"].location)
    print(response["structured_response"].temperature)

asyncio.run(main())


