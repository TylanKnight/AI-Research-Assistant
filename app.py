import streamlit as st

from src.comparison import compare_documents
from src.pdf_utils import extract_text_from_pdf
from src.question_answering import answer_question
from src.summary import summarize_text


def render_single_document_section() -> None:
    """Display the tools for analyzing one uploaded research paper."""
    st.header("Analyze One Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        key="single_document_file",
        help="Upload one text-based PDF for summarization and question answering.",
    )

    if uploaded_file is None:
        return

    try:
        text, page_count = extract_text_from_pdf(uploaded_file.getvalue())

        st.success(f"Successfully processed {uploaded_file.name}")

        page_column, character_column = st.columns(2)
        page_column.metric("Pages", page_count)
        character_column.metric("Characters extracted", f"{len(text):,}")

        if not text.strip():
            st.warning(
                "No selectable text was found. The PDF may contain scanned images "
                "and could require OCR in a later version."
            )
            return

        with st.spinner("Gemini is reading your research paper..."):
            summary = summarize_text(text)

        st.subheader("AI Summary")
        st.markdown(summary)

        st.subheader("Ask a Question About the Document")

        question = st.text_input(
            "Enter your question",
            placeholder="Example: What methodology did the paper use?",
            key="document_question",
        )

        if st.button("Ask Question", key="ask_question_button"):
            if question.strip():
                with st.spinner("Searching the document for an answer..."):
                    answer = answer_question(text, question)

                st.markdown("### Answer")
                st.markdown(answer)
            else:
                st.warning("Please enter a question before clicking the button.")

        st.divider()

        st.subheader("Extracted-text Preview")
        st.text_area(
            "First 5,000 characters",
            value=text[:5000],
            height=400,
            key="extracted_text_preview",
        )

    except ValueError as exc:
        st.error(str(exc))
    except Exception as error:
        st.error(f"Analysis error: {error}")
        print(f"Analysis error: {type(error).__name__}: {error}")


def render_comparison_section() -> None:
    """Display the tools for comparing two uploaded research papers."""
    st.header("Compare Two Documents")

    comparison_column_a, comparison_column_b = st.columns(2)

    with comparison_column_a:
        comparison_file_a = st.file_uploader(
            "Choose the first PDF",
            type=["pdf"],
            key="comparison_file_a",
        )

    with comparison_column_b:
        comparison_file_b = st.file_uploader(
            "Choose the second PDF",
            type=["pdf"],
            key="comparison_file_b",
        )

    if not st.button("Compare Documents", key="compare_documents_button"):
        return

    if comparison_file_a is None or comparison_file_b is None:
        st.warning("Please upload both PDF files before comparing them.")
        return

    try:
        with st.spinner("Extracting and comparing both documents..."):
            text_a, page_count_a = extract_text_from_pdf(
                comparison_file_a.getvalue()
            )
            text_b, page_count_b = extract_text_from_pdf(
                comparison_file_b.getvalue()
            )

            comparison = compare_documents(
                text_a=text_a,
                text_b=text_b,
                document_a_name=comparison_file_a.name,
                document_b_name=comparison_file_b.name,
            )

        st.success(
            f"Compared {comparison_file_a.name} "
            f"({page_count_a} pages) with "
            f"{comparison_file_b.name} ({page_count_b} pages)."
        )

        st.subheader("Comparison Report")
        st.markdown(comparison)

    except ValueError as exc:
        st.error(str(exc))
    except Exception as exc:
        st.exception(exc)


def main() -> None:
    """Configure and run the Streamlit application."""
    st.set_page_config(
        page_title="AI Research Assistant",
        page_icon="📚",
        layout="wide",
    )

    st.title("AI Research Assistant")
    st.write(
        "Upload academic PDFs to generate structured summaries, ask "
        "document-specific questions, and compare research papers."
    )

    render_single_document_section()

    st.divider()

    render_comparison_section()


if __name__ == "__main__":
    main()
