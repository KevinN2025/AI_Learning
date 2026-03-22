import ollama

response = ollama.chat(
        model="deepseek-r1",
        messages=[{ "role": "user", "content": "Are you available?"}]
        )
print(response["message"]["content"])

