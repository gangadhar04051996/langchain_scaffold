import asyncio
from dotenv import load_dotenv
from orchestrator_agent import run_orchestrator

load_dotenv()

async def main():
    queries = [
        "What is the weather in Arlington Arizona?"
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        response = await run_orchestrator(query)
        print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())
