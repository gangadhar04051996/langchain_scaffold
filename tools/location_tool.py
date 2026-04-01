
from langchain.tools import tool, ToolRuntime
from dataclasses import dataclass


@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str


@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    # This isn't a real location finder, just a placeholder to demonstrate how to access the user ID from the runtime context.
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"