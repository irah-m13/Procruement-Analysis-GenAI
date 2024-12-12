from pydantic import BaseModel
from typing import Dict

class QueryResponse(BaseModel):
    """
    A model representing the structure of a query response.
    """
    response: Dict
