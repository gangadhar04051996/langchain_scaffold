
# This example demonstrates how to create an MCP session and access the list of available tools.
# This is an unused code in the application
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

transport = streamable_http_client(
    url="http://127.0.0.1:8000"
)
session = ClientSession(transport)
session.initialize()
weather_tools = session.list_tools()
print("Available MCP tools:", weather_tools)