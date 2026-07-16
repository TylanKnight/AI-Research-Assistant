from io import BytesIO

import pymupdf


def extract_text_from_pdf(pdf_bytes: bytes) -> tuple[str, int]:
    """Extract readable text from PDF bytes.

    Args:
        pdf_bytes: Complete contents of an uploaded PDF file.

    Returns:
        A tuple containing the combined text and total page count.

    Raises:
        ValueError: If the uploaded file is empty or is not a valid PDF.
    """
    if not pdf_bytes:
        raise ValueError("The uploaded PDF is empty.")

    try:
        document = pymupdf.open(stream=BytesIO(pdf_bytes), filetype="pdf")
    except Exception as exc:
        raise ValueError("The uploaded file is not a readable PDF.") from exc

    pages = []
    try:
        for page in document:
            pages.append(page.get_text("text", sort=True))
        return "\n\n".join(pages).strip(), document.page_count
    finally:
        document.close()
