# weather_agent.py
import os
import requests
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
from dotenv import load_dotenv

load_dotenv()

# ----------- Weather Tool Function -----------
def get_weather(city: str) -> str:
    """
    Returns weather info for a city.
    If WEATHER_API_KEY is set, it will fetch real data.
    Otherwise, returns mocked data.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    if api_key:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        resp = requests.get(url)
        data = resp.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"The weather in {city} is {temp}°C with {condition}."
    else:
        # Mocked response
        fake_temp = hash(city) % 40  # deterministic fake temperature
        return f"The weather in {city} is {fake_temp}°C (mocked)."

# Register as a tool
get_weather_tool = function_tool(get_weather)

# ----------- Define Agent -----------
weather_agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful agent. If the user asks about weather, use the get_weather tool.",
    model=OpenAIChatCompletionsModel("gpt-4o-mini"),
    tools=[get_weather_tool],
)

# ----------- Runner -----------
if __name__ == "__main__":
    runner = Runner(weather_agent)

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        response = runner.run(user_input)
        print("Agent:", response)
