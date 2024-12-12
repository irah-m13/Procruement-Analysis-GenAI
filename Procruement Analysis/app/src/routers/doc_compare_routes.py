from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.src.service.pdf_service import PDFService

router = APIRouter()
pdf_service = PDFService()

@router.post("/compare/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a PDF file to be stored and compared later.
    """
    try:
        saved_file = pdf_service.save_uploaded_file(file)
        return JSONResponse(content={"message": "File uploaded successfully!", "file": saved_file})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/compare/query")
async def query_documents(question: str):
    """
    Queries the uploaded documents for comparisons based on the question.
    """
    try:
        result = pdf_service.compare_documents(question)
        return JSONResponse(content={"response": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
