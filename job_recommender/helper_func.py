import os
import sys
from exception.exception_handler import AppException 
from dotenv import load_dotenv
import fitz  # PyMuPDF
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

def extract_text_from_pdf(pdf_file: str) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    try:
        with fitz.open(pdf_file) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except AppException as e:
        raise AppException(e, sys) from e


def prompt_to_openai(prompt, max_tokens=600):
    """
    Send a prompt to OpenAI's API and get the response.
    
    Args:
        prompt (str): The prompt to send.
        max_tokens (int): Maximum number of tokens in the response.
        
    Returns:
        str: Response from OpenAI's API.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful job-related assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.5
        )

        return response.choices[0].message['content'] #.content
    except AppException as e:
        raise AppException(e, sys) from e


