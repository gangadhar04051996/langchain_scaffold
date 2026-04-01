from langchain_mcp_adapters.tools import MCPToolCallRequest

async def log_interceptor(request: MCPToolCallRequest, call_next):
    # BEFORE the tool call
    print(f"[INTERCEPTOR] Calling tool: {request.name}")
    print(f"[INTERCEPTOR] Arguments: {request.args}")

    result = await call_next(request)  # actual tool call happens here

    # AFTER the tool call
    print(f"[INTERCEPTOR] Result: {result}")
    return result

async def retry_interceptor(request, call_next):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return await call_next(request)
        except Exception as e:
            if attempt == max_retries - 1:
                raise  # re-raise on final attempt
            print(f"[RETRY] Attempt {attempt + 1} failed: {e}. Retrying...")
