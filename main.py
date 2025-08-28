from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document as analyze_task  # renamed to avoid conflict

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str = "data/sample.pdf"):
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_task],  # use renamed task
        process=Process.sequential,
    )
    result = financial_crew.kickoff({"query": query, "file_path": file_path})
    return result

@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query:
            query = "Analyze this financial document for investment insights"

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    print("Starting Financial Document Analyzer...")
    print("Available endpoints:")
    print("- GET  /           - Health check")
    print("- POST /analyze    - Upload and analyze document")
    uvicorn.run(app, host="127.0.0.1", port=5555, reload=False)
