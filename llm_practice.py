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

print(f"Ответ модели: {response.output_text}")
print(f"Модель: {response.model}")
print(f"Статус: {response.status}")
print(f"Входные токены: {response.usage.input_tokens}")
print(f"Выходные токены:  {response.usage.output_tokens}")
print(f"Всего токенов:{response.usage.total_tokens}")