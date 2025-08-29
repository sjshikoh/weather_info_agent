from agents import function_tool


@function_tool
def fetch_weather(city: str)-> str:
    """
    Fetch the current weather information.
    """
    return "The weather in {city} is sunny."