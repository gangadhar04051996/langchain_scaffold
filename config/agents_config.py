AGENT_CONFIGS = {
    "weather": {
        "description": "Handles weather, temperature, forecast queries",
        "keywords": ["weather", "temperature", "forecast", "rain", "sunny"],
        "tier": "low",
        "system_prompt": " You are a weather assistant.When the user asks about weather, call get_current_weather with the location.NEVER call the tool with empty arguments."
    },
    "movie": {
        "description": "Handles movie bookings, showtimes, ticket reservations",
        "keywords": ["movie", "ticket", "cinema", "book", "showtime"],
        "tier": "low",
        "system_prompt": "You are a movie booking specialist."
    },
    "email": {
        "description": "Handles sending emails, reading inbox, drafting messages",
        "keywords": ["email", "send", "inbox", "draft", "message"],
        "tier": "low",
        "system_prompt": "You are an email assistant."
    },
}