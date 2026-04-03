from langchain.agents.middleware import wrap_tool_call
from langchain_core.messages import ToolMessage


@wrap_tool_call(name="Tool call handle")
async def handle_tool_errors(request, handler):
    """
    Handle Tool Execution Errors with custom messages
    """
    print("Tool Execution Middleware: Handling tool call with request:", request.tool_call['name'] ,\
          "type: ", request.tool_call['type'])

    try:
        return await handler(request)
    except Exception as e:
        return ToolMessage(content=f"❌ An error occurred while executing the tool: {str(e)} ❌",
                           tool_call_id=request.tool_call["id"])
