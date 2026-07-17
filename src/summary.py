import os

from google import genai


def summarize_text(text: str) -> str:
    """
    Send extracted research-paper text to Gemini and return a structured summary.
    """

    if not text or not text.strip():
        raise ValueError("No text was provided for summarization.")
    
    text = text[:30000]  # Limit to first 30,000 characters to avoid exceeding API limits.  

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY was not found in the environment."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a research assistant.

Summarize the research paper text below using these sections:

1. Overview
2. Research Question or Purpose
3. Methodology
4. Key Findings
5. Limitations
6. Future Research

Use clear language and bullet points where appropriate.
Do not invent information that is not present in the paper.

Research paper text:

{text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text