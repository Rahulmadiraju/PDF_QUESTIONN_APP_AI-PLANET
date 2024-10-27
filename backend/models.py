# backend/models.py

class Question:
    def __init__(self, question_text: str):
        self.question_text = question_text
    
    def to_dict(self):
        return {"question_text": self.question_text}
