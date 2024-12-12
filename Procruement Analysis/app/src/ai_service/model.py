from llama_index.llms import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


class BaseModel:
    """
    Abstract BaseModel class to enforce consistent structure in derived classes.
    """

    def __init__(self):
        raise NotImplementedError("BaseModel is an abstract class and cannot be instantiated directly.")

    def create_model(self):
        """
        Abstract method to create a model. Must be overridden in derived classes.
        """
        raise NotImplementedError("The 'create_model' method must be implemented by subclasses.")


class AzureLLM(BaseModel):
    """
    Concrete class for creating an Azure LLM model.
    """

    def __init__(self):
        self.model_name = os.getenv("AZURE_MODEL", "gpt-35-turbo-16k")
        self.deployment_name = os.getenv("AZURE_DEPLOYMENT", "gpt-35-turbo-16k")
        self.api_key = os.getenv("AZURE_API_KEY")
        self.endpoint = os.getenv("AZURE_ENDPOINT")
        self.api_version = os.getenv("AZURE_API_VERSION", "2023-07-01-preview")

    def create_model(self):
        """
        Creates and returns an instance of the Azure LLM model.
        """
        if not all([self.api_key, self.endpoint]):
            raise ValueError("Azure API key and endpoint must be set in the environment variables.")

        return AzureOpenAI(
            model=self.model_name,
            deployment_name=self.deployment_name,
            api_key=self.api_key,
            azure_endpoint=self.endpoint,
            api_version=self.api_version
        )
