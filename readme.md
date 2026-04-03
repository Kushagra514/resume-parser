# resume-parser

A FastAPI REST API that extracts structured information from uploaded PDF resumes.

## What it does
- Extracts full text from PDF resumes
- Detects email and phone number using regex
- Matches skills against a predefined skill set
- Returns structured JSON response

## Stack
- FastAPI
- PyMuPDF (fitz)
- Python 3.11
- Poetry
- Docker
- Render

## Run Locally
```bash
git clone https://github.com/Kushagra514/resume-parser.git
cd resume-parser
poetry install
poetry run uvicorn app.main:app --reload
```

## API Endpoints

### POST /parse
Upload a PDF resume and get extracted information.

**Request:** multipart/form-data with a PDF file

**Response:**
```json
{
  "email": "kushagratewari.eng@gmail.com",
  "phone": "+91-8115144257",
  "skills": ["python", "java", "sql", "git", "machine learning"],
  "text": "full extracted resume text..."
}
```



## Live Demo
https://resume-parser-ztiy.onrender.com/docs