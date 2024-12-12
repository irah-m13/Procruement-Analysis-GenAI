from fastapi import APIRouter, UploadFile, File
from app.src.service.file_service import FileService

router = APIRouter()
file_service = FileService()

@router.post("/upload/techexcel")
async def upload_excel(file: UploadFile = File(...)):
    """
    Uploads an Excel file and processes it.
    """
    return file_service.upload_excel(file)

@router.get("/uploaded/techexcel_names")
async def get_uploaded_excel_names():
    """
    Retrieves the names of uploaded Excel files.
    """
    return file_service.get_uploaded_excel_names()
