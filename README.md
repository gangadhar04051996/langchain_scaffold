project/
│
├── main.py                          ← entry point
│
├── orchestrator/
│   └── orchestrator_agent.py        ← routes query to correct agent
│
├── agents/
│   ├── weather_agent.py             ← specialist agent
│   ├── movie_agent.py               ← specialist agent
│   ├── email_agent.py               ← specialist agent
│   └── ...17 more
│
├── mcp_servers/
│   ├── weather_mcp.py               ← MCP client for weather
│   ├── movie_mcp.py                 ← MCP client for movie
│   ├── email_mcp.py                 ← MCP client for email
│   └── ...
│
├── interceptors/
│   ├── weather_interceptor.py       ← interceptors for weather tools
│   ├── movie_interceptor.py
│   └── base_interceptor.py          ← shared log/retry logic
│── tools/
│   ├── weather_tool.py              ← tool for fetching weather data
│
├── data_models/
│   ├── response_models.py
│   └── request_models.py
│
└── config/
    └── agents_config.py             ← all agent configs in one place