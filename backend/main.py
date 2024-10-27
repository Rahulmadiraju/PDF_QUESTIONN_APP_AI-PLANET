
# backend/main.py

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils import extract_text_from_pdf
from models import Question
from database import extract_questions_from_text

app = FastAPI()

# CORS setup to allow frontend access to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint to verify server is running
@app.get("/")
async def root():
    return {"message": "Server is running!"}

# PDF upload endpoint to process the uploaded PDF and return questions
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Read and extract text from the uploaded PDF
    content = await file.read()
    text = extract_text_from_pdf(content)
    
    # Extract questions from the PDF text
    questions = extract_questions_from_text(text)
    
    # Return questions as a JSON response
    return {"questions": [q.to_dict() for q in questions]}
