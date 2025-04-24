import fitz  # PyMuPDF
import cohere
from temp import get_temp

API_KEY = "api_key"
co = cohere.Client(API_KEY)

def extract_text_from_pdf(pdf_path):
    """Extract text from the PDF"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_pdf_text(text):
    """Summarize extracted text using Cohere API"""
    try:
        response = co.chat(
            message=f"Please summarize the following text: {text}",
            model="command-r-plus",  # You can also try "command-r"
            temperature=get_temp("secure4")
        )
        return response.text
    except Exception as e:
        return f"Error summarizing PDF: {e}"

def summarize_pdf(pdf_path):
    """Main function to summarize the PDF"""
    text = extract_text_from_pdf(pdf_path)
    summary = summarize_pdf_text(text)
    return summary
