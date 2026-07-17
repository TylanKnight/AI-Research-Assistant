import os

from google import genai


def answer_question(text: str, question: str) -> str:
    """
    Answer a user's question using only the provided document text.
    """

    if not text or not text.strip():
        raise ValueError("No document text was provided.")

    if not question or not question.strip():
        raise ValueError("Please enter a question.")

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY was not found in the environment."
        )

    client = genai.Client(api_key=api_key)

    document_text = text[:30000]

    prompt = f"""
You are an AI research assistant.

Answer the user's question using only the document text provided below.

Rules:
- Do not invent information.
- If the answer is not present in the document, clearly say so.
- Give a clear and concise answer.
- Include supporting details from the document when available.

User question:
{question}

Document text:
{document_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text