# resume-parser

A FastAPI-based REST API that extracts text, email, and phone number from uploaded PDF resumes.

## Stack
- FastAPI
- PyMuPDF (fitz)
- Python 3.11
- Poetry

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
c
**Response:**
```json
{
  "email": "example@gmail.com",
  "phone": "9876543210",
  "text": "full extracted text..."
}
```

## Docs
Visit `http://127.0.0.1:8000/docs` for Swagger UI.