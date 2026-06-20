from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)

def generate_answer(
        question,
        context):

    prompt = f"""
You are an HR assistant.

Answer only using
the provided context.

Context:

{context}

Question:

{question}
"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )