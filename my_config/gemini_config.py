from decouple import config
from agents import OpenAIChatCompletionsModel, AsyncOpenAI


key = config("GEMINI_API_KEY")
base_url = config("GEMINI_BASE_URL")


client = AsyncOpenAI(api_key=key, base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)