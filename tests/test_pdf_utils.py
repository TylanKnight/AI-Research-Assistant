import pytest

from src.pdf_utils import extract_text_from_pdf


def test_empty_pdf_bytes_raise_value_error() -> None:
    with pytest.raises(ValueError, match="empty"):
        extract_text_from_pdf(b"")
