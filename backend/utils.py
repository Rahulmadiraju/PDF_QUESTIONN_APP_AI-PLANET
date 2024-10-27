
# backend/utils.py
import re
from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(content: bytes) -> str:
    reader = PdfReader(io.BytesIO(content))
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        # Remove URLs from the text
        page_text = re.sub(r'http[s]?://\S+', '', page_text)
        text += page_text
    return text
