import ollama

response = ollama.chat(
    model="Loki",
    messages=[
        {"role": "user", "content": "Explain gravity"}
    ]
)

print(response["message"]["content"])
