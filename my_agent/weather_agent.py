from agents import Agent
from my_config.gemini_config import MODEL
from my_tool.weather_tool import fetch_weather



weather_agent = Agent(
    name="Weather Assistant",
    instructions="You are a helpful assistant that provides weather information by calling fetch_weather tool.",
    model=MODEL,
    tools=[fetch_weather]
)