import ollama

response = ollama.chat(
    model="Loki",
    messages=[{"role": "user", "content": "hello"}]
)

print(response)
