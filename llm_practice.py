import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("Не найден OPENAI_API_KEY")

client = OpenAI(api_key=api_key, timeout=15.0)

response = client.responses.create(
    model="gpt-5-mini",
    input="Ответь одним словом: столица Франции?"
)

print(response.output_text)