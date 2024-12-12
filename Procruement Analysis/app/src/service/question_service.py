import os
import fitz
from haystack.nodes import QuestionGenerator


class QuestionService:
    """
    Service to handle question generation from PDFs.
    """

    def __init__(self):
        self.upload_dir = "uploaded_pdfs"
        os.makedirs(self.upload_dir, exist_ok=True)

    def upload_pdf(self, file):
        """
        Saves a PDF file to the upload directory.
        """
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        return {"message": f"PDF '{file.filename}' uploaded successfully", "path": file_path}

    def extract_text_from_pdf(self, file_path, max_length=4096, max_pages=None):
        """
        Extracts text from a PDF file.
        """
        text = ""
        with fitz.open(file_path) as pdf_doc:
            for page_num in range(min(max_pages, len(pdf_doc)) if max_pages else len(pdf_doc)):
                page = pdf_doc.load_page(page_num)
                text += page.get_text()
                if len(text) >= max_length:
                    break
        return text[:max_length]

    def generate_questions(self, filename, max_pages=None, max_length=4096):
        """
        Generates questions from the text of a PDF file.
        """
        file_path = os.path.join(self.upload_dir, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError("PDF file not found")

        text = self.extract_text_from_pdf(file_path, max_length=max_length, max_pages=max_pages)
        qg = QuestionGenerator()
        questions = qg.generate(text)
        return {"questions": questions[:5]}
