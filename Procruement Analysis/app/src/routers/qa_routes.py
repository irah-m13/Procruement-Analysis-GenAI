from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.src.service.question_service import QuestionService

router = APIRouter()
question_service = QuestionService()

@router.post("/get-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Uploads a PDF file for text extraction and question generation.
    """
    try:
        response = question_service.upload_pdf(file)
        return JSONResponse(content=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload")
async def generate_questions(filename: str, max_pages: int = None, max_length: int = 4096):
    """
    Extracts text from a PDF file and generates questions based on the content.
    """
    try:
        return question_service.generate_questions(filename, max_pages, max_length)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="PDF file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
