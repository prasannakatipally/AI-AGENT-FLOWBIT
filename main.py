# main.py

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

from mcp.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Flowbit AI Agent API is live 🚀"}

@app.post("/classify/")
async def classify_text(input_text: str = Form(...)):
    result = orchestrator.process(input_text)
    return result

@app.post("/json/")
async def classify_json(input_json: str = Form(...)):
    try:
        data = json.loads(input_json)
        result = orchestrator.process(json.dumps(data))
        return result
    except:
        return {"error": "Invalid JSON"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        text = contents.decode("utf-8")
    except:
        text = "[PDF content] (mock)"  # placeholder
    result = orchestrator.process(text)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)