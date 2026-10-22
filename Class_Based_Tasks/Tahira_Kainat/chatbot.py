import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, APIError

# Load .env from the same folder as this Python script.
load_dotenv(Path(__file__).resolve().parent / ".env")

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").strip()
api_key = os.getenv("AZURE_OPENAI_API_KEY", "").strip()
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "").strip()

# Detect missing configuration before making a request.
if not endpoint or not api_key or not deployment:
    raise ValueError(
        "Missing configuration. Check AZURE_OPENAI_ENDPOINT, "
        "AZURE_OPENAI_API_KEY, and AZURE_OPENAI_DEPLOYMENT in .env."
    )

# The .env endpoint should be the resource URL shown above.
client = OpenAI(
    base_url=f"{endpoint.rstrip('/')}/openai/v1/",
    api_key=api_key,
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Keep answers clear and concise.",
    }
]

print("Chatbot ready. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ("quit", "exit"):
        break

    if not user_input:
        continue

    # Save this turn to history only after a successful response.
    user_message = {"role": "user", "content": user_input}

    try:
        reply = ""
        print("Bot: ", end="", flush=True)

        with client.chat.completions.create(
            model=deployment,
            messages=messages + [user_message],
            temperature=0.7,
            max_tokens=800,
            stream=True,
        ) as stream:
            for chunk in stream:
                if not chunk.choices:
                    continue

                piece = chunk.choices[0].delta.content

                if piece:
                    print(piece, end="", flush=True)
                    reply += piece

        print("\n")

        messages.append(user_message)
        messages.append({"role": "assistant", "content": reply})

    except APIError as error:
        print(f"\nRequest failed ({type(error).__name__}): {error}\n")