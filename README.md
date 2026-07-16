# AI Research Assistant

A beginner-friendly Python and Streamlit application for extracting and analyzing text from academic research papers.

## Current milestone: Version 0.2

The application currently:

- accepts one PDF upload;
- extracts selectable text with PyMuPDF;
- reports page and character counts;
- displays a text preview;
- handles empty and unreadable files.

AI summarization, question answering, paper comparison, citations, and cloud deployment are planned for later milestones.

## Why this project exists

Graduate students often spend significant time organizing and reviewing academic papers. This project explores how document-processing and AI tools can support that workflow while demonstrating Python, software design, testing, documentation, and Git version control.

## Project structure

```text
AI-Research-Assistant/
├── app.py
├── src/
│   ├── __init__.py
│   └── pdf_utils.py
├── tests/
│   └── test_pdf_utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally

1. Create a virtual environment:

   Windows:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   streamlit run app.py
   ```

4. Open the local address Streamlit displays in the terminal.

## Run tests

```bash
pytest
```

## Roadmap

- [x] Create repository foundation
- [x] Add PDF upload and text extraction
- [ ] Generate structured paper summaries
- [ ] Ask questions about an uploaded paper
- [ ] Compare two papers
- [ ] Export research notes
- [ ] Add more automated tests
- [ ] Deploy a public demo

## License

MIT
