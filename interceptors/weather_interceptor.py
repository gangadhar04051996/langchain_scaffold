from langchain_mcp_adapters.tools import MCPToolCallRequest

def get_validators_for_tool(tool_name: str):
    # get_current_weather is from the mcp server, when using validator interceptor,
    # it will call this function to get the validators for the tool
    validators = {
        "get_current_weather": [
            validate_weather_args
        ],
    }

    return validators[tool_name]


async def validate_weather_args(arguments: dict):
    if not arguments.get("location"):
        raise ValueError("[VALIDATION] get_current_weather requires a 'location'")



async def validation_interceptor(request:MCPToolCallRequest, call_next):
    # request.name give the tool name then from tool name we are getting the validators.
    validators = get_validators_for_tool(request.name)  # returns a list

    for validator in validators:             # ✅ loop through each
        await validator(request.args)   # ✅ call it with arguments

    return await call_next(request)



