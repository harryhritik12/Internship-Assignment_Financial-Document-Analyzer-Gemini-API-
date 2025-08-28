Financial Document Analyzer

An AI-powered tool for analyzing financial reports (PDFs), performing investment analysis, and risk assessments.
This project integrates Google Gemini API as the core LLM engine.

🚨 Bugs Found & Fixes
1. Dependency Conflicts

Issue: Multiple version conflicts between crewai, opentelemetry, and onnxruntime.

Fix:

Loosened strict version pins in requirements.txt.

Ensured compatibility by upgrading crewai and crewai-tools together.

2. @tools vs @tool Decorator

Issue: Using @tools caused:

TypeError: 'module' object is not callable


Fix: Correct decorator is @tool (singular) from crewai.

from crewai import tool

class FinancialDocumentTool:
    @tool("read_data_tool")
    async def read_data_tool(path="data/sample.pdf"):
        ...

3. Localhost Reload Issues

Issue: Local server with auto-reload created conflicts while testing.

Fix: Disabled reload with uvicorn main:app --reload=false.

Alternatively, switched to API-based usage with Gemini to avoid local LLM runtime.

4. Pdf Not Defined

Issue:

NameError: name 'Pdf' is not defined


Fix: Installed and used unstructured or pypdf for parsing PDFs:

pip install pypdf

from pypdf import PdfReader

5. Migration to Gemini API

Issue: Ollama/local models required large downloads & conflicted dependencies.

Fix: Integrated Gemini API (google-generativeai).

⚙️ Setup & Usage
1. Clone Repository
git clone https://github.com/your-username/financial-document-analyzer.git
cd financial-document-analyzer

2. Setup Virtual Environment
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_google_gemini_api_key

5. Run Application
python main.py

🔑 Gemini API Integration

Install:

pip install google-generativeai


Usage in code (llm.py):

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text


Example:

print(ask_gemini("Summarize the financial risks in Q2 report."))

📖 API Documentation
1. Financial Document Tool

Endpoint: read_data_tool

Input: PDF path (default: data/sample.pdf)

Output: Cleaned text content of PDF.

2. Investment Tool

Endpoint: analyze_investment_tool

Input: Financial document data (string)

Output: Investment insights (future expansion).

3. Risk Tool

Endpoint: create_risk_assessment_tool

Input: Financial document data (string)

Output: Risk analysis (future expansion).

4. Gemini Query Tool

Function: ask_gemini(prompt: str)

Input: Free-form question or analysis prompt.

Output: AI-generated insights using Gemini API.

🚀 Roadmap

✅ Replace Ollama with Gemini API

✅ Fix dependency conflicts
