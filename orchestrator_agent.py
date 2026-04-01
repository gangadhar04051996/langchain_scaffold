from langchain.agents import create_agent
from langchain.tools import tool
from agents.weather_agent import weather_main
import asyncio
from config.agents_config import AGENT_CONFIGS
from models_config.get_model_object import get_openai_model

def build_orchestrator_tools():

    @tool()
    async def weather_agent(query:str):
        """Handles weather, temperature, forecast queries."""
        return await weather_main(query)


    return [
        weather_agent,
    ]


async def run_orchestrator(query:str):
    tools = build_orchestrator_tools()

    orchestrator = create_agent(
        model=get_openai_model(tier="low"),
        tools=tools,
        system_prompt="""
        You are an orchestrator agent. Your job is to route the user's query to the appropriate agent tool.
        If the user's query is about weather, call the weather_agent tool with the query as an argument.
        Always call the tool with the appropriate arguments.
        """,
    )
    result = await orchestrator.ainvoke({
        "messages": [{"role": "user", "content": query}]
    })
    return result["messages"][-1].content