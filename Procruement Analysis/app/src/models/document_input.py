from pydantic import BaseModel, Field

class DocumentInput(BaseModel):
    """
    A model representing input for document processing.
    """
    question: str = Field(..., description="The question to query the document.")
