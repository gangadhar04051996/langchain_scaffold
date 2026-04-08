from langchain.agents import create_agent
from langchain.tools import tool
from agents.weather_agent import weather_main
from tools.tools_middlewear import LoggingMiddleware
from models_config.get_model_object import get_openai_model, get_ollama_model
from langchain_core.messages import HumanMessage, SystemMessage

def build_orchestrator_tools():

    @tool()
    async def weather_agent(query:str):
        """Handles weather, temperature, forecast queries."""
        return await weather_main(query)
    return [
        weather_agent,
    ]


ollama_model_low = get_ollama_model(tier="local_low")
ollama_model_med = get_ollama_model(tier="local_medium")
ollama_model_cloud_med = get_ollama_model(tier="cloud_medium")
openai_model_low = get_openai_model(tier="low")


async def run_orchestrator(query:str):
    tools = build_orchestrator_tools()

    orchestrator_agent = create_agent(
        model=ollama_model_cloud_med,
        tools=tools,
        middleware=[LoggingMiddleware()],
        system_prompt= SystemMessage(
            content= [
                {
                    "type": "text",
                    "text": """
                            You are an orchestrator agent. Your job is to route the user's query to the appropriate agent tool.
                            If the user's query is about weather, call the weather_agent tool with the query as an argument.
                            Always call the tool with the appropriate arguments.
                    """,
                }
            ]
        ),
    )
    result = await orchestrator_agent.ainvoke({
        "messages": [{"role": "user", "content": query}]
    })
    return result["messages"][-1].content