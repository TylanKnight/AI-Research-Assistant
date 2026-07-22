from .gemini_service import GeminiService


MAX_DOCUMENT_CHARS = 30000


def summarize_text(text: str) -> str:
    """
    Generate a structured summary for a research paper.
    """

    if not text or not text.strip():
        raise ValueError("No text was provided for summarization.")

    document_text = text[:MAX_DOCUMENT_CHARS]

    prompt = f"""
You are an expert AI research assistant.

Summarize the research paper using the following sections.

# Overview

# Research Question or Purpose

# Methodology

# Key Findings

# Limitations

# Future Research

Instructions:

- Use only the document.
- Never invent information.
- Use headings.
- Use bullet points when appropriate.
- Keep the summary clear and concise.

Research Paper:

{document_text}
"""

    service = GeminiService()

    return service.generate(prompt)