
#loading api key file using load_dotenv
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

#print(api_key is not None)
client = OpenAI(api_key=api_key)

response = client.responses.create(
model="gpt-4o-mini",
instructions="You are a helpful AI assistant. Answer clearly and briefly.",
input="Explain what an api is in two sentences"
)


print(response.output_text )


