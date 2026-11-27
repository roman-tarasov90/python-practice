import os
from openai import OpenAI



def ask_ai(
    client: OpenAI, 
    prompt: str, 
    model: str = "gpt-5-mini"
) -> str:
    return client.responses.create(
        model=model,
        input=prompt
    ).output_text

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("Не найден OPENAI_API_KEY")

    client = OpenAI(api_key=api_key, timeout=15.0)

    print(ask_ai(client, "Какая столица Украины?"))
    print(ask_ai(client, "Сколько будет 5 + 5?"))