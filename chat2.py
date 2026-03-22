import ollama

response = ollama.chat(
        model="deepseek-r1",
        messages=[{ "role": "system", "content": "You are a System Engineer"},
        {"role": "user", "content": "Give me the 5 most important acronyms I should know in IT"}]
        )
print(response["message"]["content"])

