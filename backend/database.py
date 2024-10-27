# backend/database.py

from models import Question

def extract_questions_from_text(text: str):
    # Basic logic to split text into questions based on question marks
    lines = text.splitlines()
    questions = []
    
    for line in lines:
        if "?" in line:
            questions.append(Question(line.strip()))
    
    return questions
