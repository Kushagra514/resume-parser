from fastapi import FastAPI, UploadFile, File
from app.parser import parse_resume

app = FastAPI()
@app.post("/parse")

async def parse(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    return parse_resume(pdf_bytes)