from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    store=True,
    messages=[{"role": "user", "content": "write a haiku about ai"}],
)

print(completion.choices[0].message)
