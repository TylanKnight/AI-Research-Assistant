import os

from google import genai


def compare_documents(
    text_a: str,
    text_b: str,
    document_a_name: str = "Document A",
    document_b_name: str = "Document B",
) -> str:
    """
    Compare two documents and return a structured AI-generated report.
    """

    if not text_a or not text_a.strip():
        raise ValueError(f"No text was extracted from {document_a_name}.")

    if not text_b or not text_b.strip():
        raise ValueError(f"No text was extracted from {document_b_name}.")

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY was not found in the environment."
        )

    client = genai.Client(api_key=api_key)

    document_a_text = text_a[:30000]
    document_b_text = text_b[:30000]

    prompt = f"""
You are an AI research assistant.

Compare the two documents below and create a structured comparison report.

Use these sections:

1. Overall Focus
2. Main Similarities
3. Main Differences
4. Research Questions or Objectives
5. Methodology Comparison
6. Findings or Conclusions
7. Limitations
8. Overall Evaluation

Rules:
- Base the comparison only on the provided document text.
- Do not invent missing information.
- Clearly state when a section is not discussed in one or both documents.
- Refer to the documents by their provided names.
- Use clear headings and bullet points where appropriate.
- Keep the comparison balanced and objective.

{document_a_name}:

{document_a_text}

{document_b_name}:

{document_b_text}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty comparison response.")

    return response.text