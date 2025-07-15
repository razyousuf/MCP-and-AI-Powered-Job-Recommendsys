import os
import sys
from exception.exception_handler import AppException 
from dotenv import load_dotenv
import fitz  # PyMuPDF

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
