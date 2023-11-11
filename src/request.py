from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0613:personal::8JlDMvm9",
    messages=[
        {"role": "system", "content": "あなたは天才機械学習エンジニアです. "},
        {"role": "user", "content": "LangChainとは何ですか？"}
    ]
)

print(response.choices[0].message)