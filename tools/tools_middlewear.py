from langchain.agents.middleware import AgentMiddleware, ToolCallRequest, wrap_tool_call as wrap_tool_call_decorator
from langchain_core.messages import ToolMessage
from typing import Callable


# this is the old way example.
@wrap_tool_call_decorator(name="Tool call handle")
async def handle_tool_errors(request, handler):
    """
    Handle Tool Execution Errors with custom messages
    """
    print("Tool Execution Middleware: Handling tool call with request:", request.tool_call['name'] ,\
          "type: ", request.tool_call['type'])

    try:
        result = await handler(request)
        print(f"[Middleware] Tool Executed")
        return result
    except Exception as e:
        return ToolMessage(content=f"❌ An error occurred while executing the tool: {str(e)} ❌",
                           tool_call_id=request.tool_call["id"])

class LoggingMiddleware(AgentMiddleware):
    # Async version for async agents:
    async def awrap_tool_call(
        self,
        request: ToolCallRequest,
        handler: Callable[[ToolCallRequest], ToolMessage],
    ) -> ToolMessage:
        tool_name = request.tool_call["name"]
        tool_args = request.tool_call["args"]
        print(f"[Middleware] Calling tool: {tool_name} with input: {tool_args}")
        try:
            result = await handler(request)
            print(f"[Middleware] Tool {tool_name} returned: {result.content}")
            return result
        except Exception as e:
            print(f"[Middleware] Tool {tool_name} failed: {e}")
            raise