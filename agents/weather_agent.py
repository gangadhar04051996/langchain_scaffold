from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from data_models.response_models import TemperatureResponseModel
import uuid
from config.agents_config import AGENT_CONFIGS
from models_config.get_model_object import get_openai_model, get_anthropic_model

load_dotenv()
from mcp_servers.weather_mcp import get_weather_tools
import asyncio
from dataclasses import dataclass


# storing the memory
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()


model_tier = AGENT_CONFIGS['weather']['tier']
system_prompt = AGENT_CONFIGS['weather']['system_prompt']

async def weather_main(query):
    tools = await get_weather_tools()
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    agent = create_agent(
        model=get_openai_model(tier=model_tier),
        tools=tools,
        system_prompt=system_prompt,
        checkpointer=checkpointer,
        response_format= TemperatureResponseModel
    )

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": query}]},
        config = config
    )

    print(response["structured_response"].location)
    print(response["structured_response"].temperature)
    return {
        "location": response["structured_response"].location,
        "temperature": response["structured_response"].temperature,
    }
