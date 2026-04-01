import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from interceptors.weather_interceptor import (
    validation_interceptor
)
from interceptors.base_interceptors import (
log_interceptor,
retry_interceptor
)

async def get_weather_tools():
    """
    This is an MCP Server that returns the tools for weather information.
    :return:
    """
    client = MultiServerMCPClient(
        {
            "weather_server": {
                "transport": "streamable_http",
                "url": "http://localhost:8000/mcp",
            }
        },
        tool_interceptors=[
            log_interceptor,
            validation_interceptor,
            retry_interceptor
        ]
    )
    return await client.get_tools()
