import streamlit as st

from src.pdf_utils import extract_text_from_pdf
from src.summary import summarize_text
from src.question_answering import answer_question


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

st.title("AI Research Assistant")
st.write(
    "Upload an academic PDF to extract its text, generate an AI-powered "
    "summary, and inspect the original text."
)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
    help="Version 0.2 accepts one PDF at a time.",
)

if uploaded_file is not None:
    try:
        text, page_count = extract_text_from_pdf(uploaded_file.getvalue())

        st.success(f"Successfully processed {uploaded_file.name}")
        col1, col2 = st.columns(2)
        col1.metric("Pages", page_count)
        col2.metric("Characters extracted", f"{len(text):,}")

        if text.strip():
            with st.spinner("Gemini is reading your research paper..."):
                summary = summarize_text(text)

            st.subheader("AI Summary")
            st.markdown(summary)

            st.subheader("Ask a Question About the Document")

            question = st.text_input(
                "Enter your question",
                placeholder="Example: What methodology did the paper use?",
)

            if st.button("Ask Question"):
                if question.strip():
                    with st.spinner("Searching the document for an answer..."):
                        answer = answer_question(text, question)

                    st.markdown("### Answer")
                    st.markdown(answer)
                else:
                    st.warning("Please enter a question before clicking the button.")

            st.divider()

            st.subheader("Extracted-text preview")
            st.text_area(
                "First 5,000 characters",
                value=text[:5000],
                height=400,
            )
        else:
            st.warning(
                "No selectable text was found. The PDF may contain scanned images "
                "and could require OCR in a later version."
            )
    except ValueError as exc:
        st.error(str(exc))
    except Exception as exc:
        st.error(
            "The document could not be summarized. Please try again or use "
            "a different PDF."
        )
            
