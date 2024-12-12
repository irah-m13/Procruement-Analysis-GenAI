import logging


# Logger Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Custom Exceptions
class BaseAppException(Exception):
    """
    Base exception class for application-specific exceptions.
    """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class FileProcessingError(BaseAppException):
    """
    Exception raised for errors during file processing.
    """
    def __init__(self, message="Error occurred during file processing"):
        super().__init__(message)


class DatabaseConnectionError(BaseAppException):
    """
    Exception raised for database connection issues.
    """
    def __init__(self, message="Failed to connect to the database"):
        super().__init__(message)


class QueryExecutionError(BaseAppException):
    """
    Exception raised for issues during query execution.
    """
    def __init__(self, message="Error occurred while executing the query"):
        super().__init__(message)


class PDFProcessingError(BaseAppException):
    """
    Exception raised for errors during PDF processing.
    """
    def __init__(self, message="Error occurred while processing the PDF"):
        super().__init__(message)


# Example usage
if __name__ == "__main__":
    try:
        # Simulate a database connection error
        raise DatabaseConnectionError()
    except DatabaseConnectionError as e:
        logger.error(f"Database error: {e.message}")
