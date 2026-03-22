import ollama

# Load system prompt from file if available
try:
    with open("system_prompt.txt", "r") as f:
        system_prompt = f.read().strip()
except:
    system_prompt = "You are Loki, a mischievous trickster AI who enjoys clever lies, riddles, and playful deception."

# Conversation memory
messages = [
    {"role": "system", "content": system_prompt}
]

print("\n🜏 Loki AI initialized")
print("Commands: /reset  /exit\n")

while True:
    try:
        user_input = input("You: ")

        # Exit command
        if user_input.lower() in ["/exit", "/quit"]:
            print("Loki: Until next time, mortal.")
            break

        # Reset memory
        if user_input.lower() == "/reset":
            messages = [{"role": "system", "content": system_prompt}]
            print("Memory reset.\n")
            continue

        # Add user message
        messages.append({
            "role": "user",
            "content": user_input
        })

        print("\nLoki:", end=" ", flush=True)

        # Stream response from Ollama
        stream = ollama.chat(
            model="Loki",
            messages=messages,
            stream=True,
            options={"temperature": 0.7}
        )

        assistant_reply = ""

        for chunk in stream:
            message = chunk.get("message")

            if message:
                content = message.get("content", "")
                print(content, end="", flush=True)
                assistant_reply += content

        print("\n")

        # Save assistant reply to conversation memory
        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        break

    except Exception as e:
        print("\nError:", e)

