# PDF Question Extractor

A full-stack application that allows users to upload PDF documents, automatically extract questions from the document's content, and display these questions on the frontend.


## Overview
The PDF Question Extractor is a tool for uploading PDF documents and automatically extracting questions from the text. This project is intended for quick analysis of content with a specific focus on question identification, using Natural Language Processing (NLP) patterns.

## Features
- **PDF Upload**: Users can upload PDF files for text analysis.
- **Automatic Question Extraction**: Extracts sentences resembling questions from the PDF content.
- **Display of Extracted Questions**: The extracted questions are displayed on the frontend in an interactive UI.
- **Error Handling**: Basic error handling for unsupported file types and backend processing issues.

## Technologies Used
- **Frontend**: React.js
- **Backend**: FastAPI
- **Database**: SQLite (optional for metadata storage)
- **File Processing**: PyPDF2 for PDF text extraction
- **Styles**: CSS for custom styling

## Application Architecture
The PDF Question Extractor application is a full-stack project with a FastAPI backend and a React frontend. Here’s how the architecture is organized:

### 1. Frontend (React): 
- **UI Components:** The frontend consists of React components that handle the user interface and interactions. Key components include:
       
    - **Upload Component (```Upload.js```):**  Manages file uploads and sends the selected PDF to the backend.

    - **Question Component (```Question.js```):** Displays each extracted question returned from the backend.

- **Main Application Component (```App.js```):** Orchestrates the application layout and handles the state of extracted questions, passing data between the Upload and Question components.

- **Styling:** Custom styles are defined in ```App.css``` for a clean and user-friendly interface.

### 2. Backend (FastAPI)
- **API Endpoints:**

    - **```/upload-pdf```:** Accepts PDF file uploads, extracts text, identifies question-like content, and returns the questions as a JSON response.

    - **Root Endpoint (```/```):** Verifies that the server is running.

- **PDF Processing:**
    - The backend uses **PyPDF2** to extract text from the uploaded PDF files.
    - In ```database.py```, the extracted text is analyzed to identify questions based on keywords and punctuation patterns.
- **Question Model:**

    -  A simple class in ```models.py``` is used to structure and format the extracted questions before they are sent back to the frontend.

### 3. Communication Flow
- **Frontend to Backend:**
 The React frontend sends PDF files to the FastAPI backend through the ```/upload-pdf``` endpoint.

- **Backend Processing:** The backend processes the PDF, extracts and formats questions, and responds with a JSON array of question objects.

- **Data Display on Frontend:** The frontend displays the extracted questions in an interactive format, updating the UI dynamically after each upload.


## Setup Instructions

### Prerequisites
- **Node.js** (for running the frontend)
- **Python 3** (for the FastAPI backend)
- **pip** (Python package installer)
- **Create a Virtual environment:**
   ```
   python -m venv env
   env\Scripts\activate
   ```



## Backend Setup
1. Navigate to the backend directory:

   ```bash
   cd backend 
   ```
2. Install the required Python packages:

   ```
   pip install fastapi uvicorn PyPDF2
   ```
3. Start the backend server:

   ```
   uvicorn main:app --reload --port 8080
   ```
   - **The backend will run on ```http://127.0.0.1:8080```**

## Frontend Setup
1. Open a new terminal and navigate to the frontend directory:

   ```
   cd frontend
   ```
2. Install frontend dependencies:

   ```
   npm install
   ```
3. Start the React frontend server:

   ```
   npm start
   ```
   - **The frontend will run on ```http://localhost:3000```**
   

## Usage
Open the frontend app in a browser at ```http://localhost:3000``` .
Click the Upload PDF button, select a PDF file, and wait for processing.
The extracted questions will appear below the upload button.

## API Documentation
POST /upload-pdf
Description: 

Upload a PDF file, extract text, and return identified questions.

Request: Multipart form data containing a PDF file.

Response: JSON object with extracted questions.

### Example Response:

```json
{
  "questions": [
    {
      "question_text": "What is your name?"
    },
    {
      "question_text": "What do you do for a living?"
    },
    {
      "question_text": "How are you ?"
    }
  ]
}
```
