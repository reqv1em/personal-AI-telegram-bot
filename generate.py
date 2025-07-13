from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

async def ai_generate(text: str):
  try:
    completion = await client.chat.completions.create(
    model=os.getenv("OPENROUTER_MODEL"),
    messages=[
      {"role": "user", "content": "priority answer lang - ru:" + text}
    ]
    )
    print(completion)
    return completion.choices[0].message.content
  except Exception as e:
    error_text = f"❌ Произошла ошибка при генерации ответа:\n{str(e)}"
    print(error_text)
    return error_text



