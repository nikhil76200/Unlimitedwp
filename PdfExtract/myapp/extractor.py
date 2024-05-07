# text_extractor/extractor.py

import os
import docx
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_doc(doc_path):
    doc = docx.Document(doc_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def extract_text_from_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext.lower() == '.docx':
        return extract_text_from_doc(file_path)
    else:
        return None
