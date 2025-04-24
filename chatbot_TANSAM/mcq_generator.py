import fitz  # PyMuPDF
import cohere

API_KEY = "your_api_key"
co = cohere.Client(API_KEY)

def extract_text_from_pdf(pdf_path):
    """Extract text from the PDF"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def generate_mcqs_from_text(text):
    """Generate MCQs using Cohere API"""
    try:
        response = co.chat(
            message=f"Generate multiple choice questions (MCQs) based on this text: {text}",
            model="command-r-plus",  # You can also try "command-r"
            temperature=0.7
        )
        return response.text
    except Exception as e:
        return f"Error generating MCQs: {e}"

def create_mcqs_from_pdf(pdf_path):
    """Main function to generate MCQs from PDF"""
    text = extract_text_from_pdf(pdf_path)
    mcqs = generate_mcqs_from_text(text)
    return mcqs
