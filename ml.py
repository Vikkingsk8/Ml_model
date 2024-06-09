

from groq import Groq

client = Groq(
    api_key="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",
)

data = "instruction.pdf"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"что о чем файл {data}",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)