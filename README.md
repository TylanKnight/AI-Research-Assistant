# 🤖 AI Research Assistant

<p align="center">
<img src="assets/banner.png" width="100%">
</p>

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Live-success)

An AI-powered research assistant built with Python, Streamlit, and Google Gemini.

## 🚀 Live Demo

https://ai-research-assistant-tylan.streamlit.app/

## ✨ Features

- Upload PDF research papers
- AI-generated summaries
- Ask questions about uploaded documents
- Compare two research papers
- Deployed on Streamlit Community Cloud

## 📸 Application Walkthrough

### Upload & Analyze
![Home](assets/app-home.png)

### AI Summary
![Summary](assets/app-summary.png)

### Ask Questions
![Questions](assets/app-question.png)

### Compare Papers
![Comparison](assets/app-comparison.png)

### Comparison Report
![Comparison Details](assets/app-comparison-details.png)

## 🏗️ Architecture

```text
Streamlit UI → PDF Extraction → Gemini Service → Summary / Q&A / Comparison
```

## 🛠️ Tech Stack

- Python 3.14
- Streamlit
- Google Gemini API
- PyPDF
- Git & GitHub

## ⚙️ Installation

```bash
git clone https://github.com/TylanKnight/AI-Research-Assistant.git
cd AI-Research-Assistant
pip install -r requirements.txt
streamlit run app.py
```

Environment variable:

```text
GEMINI_API_KEY=your_api_key
```

## 👨‍💻 About

Created by **Tylan Knight** to demonstrate Python development, AI integration, modular software architecture, and cloud deployment.

⭐ If you found this project useful, consider starring the repository!
