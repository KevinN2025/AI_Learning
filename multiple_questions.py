import ollama

questions = [
    "Explain Roman engineering",
    "Why were Roman roads important?",
    "How did aqueducts work?",
    "What made the Roman military effective?"
]

for q in questions:

    response = ollama.chat(
        model="deepseek-r1",
        messages=[{"role": "user", "content": q}]
    )

    print("\nQUESTION:", q)
    print("ANSWER:", response["message"]["content"])
