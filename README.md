Financial Document Analyzer (Gemini API)

This project is a financial document analyzer that extracts text from PDF files and uses Google Gemini API to generate insights such as investment analysis, risk assessment, and key highlights.

🐞 Bugs Found & Fixes
1. TypeError: 'module' object is not callable

Cause: Used @tools(...) from crewai_tools, but tools is a module, not a decorator.

Fix: Removed CrewAI decorators and switched to Gemini API directly.

2. ImportError: cannot import name 'tool' from 'crewai'

Cause: Wrong import; crewai doesn’t expose tool.

Fix: Removed CrewAI dependency entirely.

3. Pdf is not defined

Cause: Tried to use Pdf without importing any PDF library.

Fix: Replaced with PyPDF2
 to read PDFs.

4. Multiple dependency conflicts (FastAPI + CrewAI + Opentelemetry, etc.)

Cause: Version mismatches across CrewAI ecosystem.

Fix: Removed all conflicting packages, kept only minimal dependencies (PyPDF2, google-generativeai, dotenv).

✅ Final solution: Gemini API + PyPDF2 → Lightweight, no conflicts, works reliably.

⚙️ Setup & Usage
1. Clone the repo
git clone https://github.com/yourusername/financial-document-analyzer.git
cd financial-document-analyzer

2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Add your Gemini API Key

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

5. Place PDF File

Put your financial document in data/sample.pdf.

6. Run
python main.py

📄 Example Output
📊 Financial Analysis Result:

1. Investment Insights:
   - Strong revenue growth ...
   - Operating margin improved ...

2. Risk Assessment:
   - High debt-to-equity ratio ...
   - Market volatility concerns ...

3. Key Highlights:
   - Dividend increase ...
   - Expansion into new markets ...

📖 API Documentation (Gemini Integration)
Endpoint Used

Gemini is accessed via the Google Generative AI Python SDK
.

Model: gemini-1.5-flash

Method: generate_content(prompt)

Prompt Structure
prompt = f"""
You are a financial analyst. Analyze the following financial document:
---
{pdf_text}
---
Provide:
1. Investment insights
2. Risk assessment
3. Key highlights
"""

Response

The model returns structured natural language text:

{
  "text": "Investment Insights: ... Risk Assessment: ... Key Highlights: ..."
}

✅ Tech Stack

Python 3.10+

PyPDF2
 → Extracts text from PDF

google-generativeai
 → Gemini API client

python-dotenv
 → Manage environment variables

🚀 Future Improvements

Add FastAPI endpoint for uploading PDFs

Store results in a database

Support multi-file batch analysis

Would you like me to also add FastAPI routes in the README (API-style usage) so it looks like a proper developer API doc, or keep it focused on script usage only?

You said:
how de acticvate .env file
ChatGPT said:

Good question 👍
A .env file isn’t something you activate — it’s just a plain text file that stores environment variables.

Your code loads it using:

from dotenv import load_dotenv
load_dotenv()


This means when you run python main.py, the .env file values (like GEMINI_API_KEY) get injected into your Python environment automatically.

📌 To “deactivate” or stop using .env

You have a few options:

Remove the .env file
Simply delete it:

rm .env      # Linux/Mac
del .env     # Windows


Comment out load_dotenv()
In main.py (or wherever you load it), remove or comment:

# load_dotenv()


Unset environment variables manually

Linux/Mac:

unset GEMINI_API_KEY


Windows (CMD):

set GEMINI_API_KEY=


Windows (PowerShell):

Remove-Item Env:\GEMINI_API_KEY


⚠️ But usually, you don’t need to “deactivate” it.
If you want to switch API keys or stop using Gemini, you can just edit .env and remove/change the variable.

Do you want me to show you how to switch from .env → system environment variables (so you don’t