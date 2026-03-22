import ollama

# Load system prompt from file if available
try:
    with open("system_prompt.txt", "r") as f:
        system_prompt = f.read().strip()
except:
    system_prompt = "You are Loki, a mischievous trickster AI who enjoys clever lies, riddles, and playful deception."

# Conversation history
messages = [
    {"role": "system", "content": system_prompt}
]

print("\n🜏 Loki AI initialized")
print("Commands: /reset  /exit\n")

while True:
    try:
        user_input = input("You: ")

        # Commands
        if user_input.lower() in ["/exit", "/quit"]:
            print("Loki: Until next time, mortal.")
            break

        if user_input.lower() == "/reset":
            messages = [{"role": "system", "content": system_prompt}]
            print("Memory reset.")
            continue

        # Add user message
        messages.append({
            "role": "user",
            "content": user_input
        })

        print("\nLoki:", end=" ", flush=True)

        # Stream response
        stream = ollama.chat(
            model="loki",
            messages=messages,
            stream=True
        )

        assistant_reply = ""

        for chunk in stream:
            content = chunk["message"]["content"]
            assistant_reply += content
            print(content, end="", flush=True)

        print("\n")

        # Save assistant reply to memory
        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        break

    except Exception as e:
        print("\nError:", e)
