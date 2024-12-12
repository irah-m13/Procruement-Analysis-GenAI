from pydantic import BaseModel

class BaseAppModel(BaseModel):
    """
    Base class for application models, providing common functionality.
    """
    class Config:
        arbitrary_types_allowed = True
        anystr_strip_whitespace = True
