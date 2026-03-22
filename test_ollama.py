import ollama

response = ollama.chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": "Explain why the Roman road network was important."
        }
    ]
)

print(response["message"]["content"])
