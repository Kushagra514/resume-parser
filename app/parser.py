import fitz
import re

def parse_resume(pdf_bytes: bytes) -> dict:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page in doc:
                text += page.get_text()
        email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        phone_match = re.search(r'[\+]?[\d\s\-]{10,13}', text)
        email = email_match.group() if email_match else None
        phone = phone_match.group() if phone_match else None

        return {
        "email": email,
        "phone": phone,
        "text": text
        }