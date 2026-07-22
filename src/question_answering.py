from .gemini_service import GeminiService


MAX_DOCUMENT_CHARS = 30000


def answer_question(text: str, question: str) -> str:
    """
    Answer a user's question using only the provided document.
    """

    if not text or not text.strip():
        raise ValueError("No document text was provided.")

    if not question or not question.strip():
        raise ValueError("Please enter a question.")

    document_text = text[:MAX_DOCUMENT_CHARS]

    prompt = f"""
You are an AI research assistant.

Answer the user's question using ONLY the provided document.

Rules:

- Never invent information.
- If the answer cannot be found, clearly say so.
- Keep the response concise.
- Quote important facts from the document when appropriate.

Question:

{question}

Document:

{document_text}
"""

    service = GeminiService()

    return service.generate(prompt)