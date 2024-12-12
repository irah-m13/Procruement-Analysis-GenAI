import os
from typing import List

class FileService:
    """
    Service to handle file-related operations.
    """
    def __init__(self):
        self.uploaded_excels = []

    def upload_excel(self, file):
        """
        Handles Excel file upload and processes it.
        """
        directory = "Summ"
        os.makedirs(directory, exist_ok=True)
        file_location = f"./{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        table_name = file.filename.split('.')[0]
        self.uploaded_excels.append(table_name)
        return {"message": f"Excel file '{file.filename}' uploaded and saved under '{file_location}'."}

    def get_uploaded_excel_names(self) -> List[str]:
        """
        Retrieves the names of all uploaded Excel files.
        """
        return {"uploaded_excels": self.uploaded_excels}
