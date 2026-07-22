from .gemini_service import GeminiService


MAX_DOCUMENT_CHARS = 15000


def _create_snapshot(
    service: GeminiService,
    text: str,
    document_name: str,
) -> str:
    """
    Creates a concise snapshot of a document that can later be compared.
    """

    prompt = f"""
You are an AI research assistant.

Analyze the document below.

Return ONLY:

1. Main Topic
2. Research Purpose
3. Methodology
4. Key Findings
5. Conclusions
6. Limitations

Keep the response under 500 words.

Document Name:
{document_name}

Document:

{text[:MAX_DOCUMENT_CHARS]}
"""

    return service.generate(prompt)


def compare_documents(
    text_a: str,
    text_b: str,
    document_a_name: str = "Document A",
    document_b_name: str = "Document B",
) -> str:
    """
    Compare two research papers using compact AI-generated snapshots.
    """

    if not text_a or not text_a.strip():
        raise ValueError(f"No text was extracted from {document_a_name}.")

    if not text_b or not text_b.strip():
        raise ValueError(f"No text was extracted from {document_b_name}.")

    service = GeminiService()

    snapshot_a = _create_snapshot(
        service,
        text_a,
        document_a_name,
    )

    snapshot_b = _create_snapshot(
        service,
        text_b,
        document_b_name,
    )

    comparison_prompt = f"""
You are an AI research assistant.

Compare these two research paper summaries.

=========================

{document_a_name}

{snapshot_a}

=========================

{document_b_name}

{snapshot_b}

=========================

Create a professional comparison report with these sections:

# Overall Focus

# Main Similarities

# Main Differences

# Research Objectives

# Methodology Comparison

# Findings Comparison

# Strengths

# Weaknesses

# Overall Evaluation

Rules:

- Base your comparison ONLY on the summaries above.
- Do not invent information.
- Use headings.
- Use bullet points whenever appropriate.
- Be objective and balanced.
"""

    return service.generate(comparison_prompt)