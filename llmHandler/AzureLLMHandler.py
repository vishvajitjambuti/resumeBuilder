
import os
from dotenv import load_dotenv

import openai
load_dotenv()

class AzureLLMHandler:
    """Handler for Azure OpenAI LLM interactions."""

    def __init__(self, model_name: str = None):
        self.model_name = model_name
        self.Azure_OpenAI_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.Azure_OpenAI_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.Azure_OpenAI_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "azure_openai" )
        self.client = openai.AzureOpenAI(
            azure_endpoint=self.Azure_OpenAI_endpoint,
            api_key=self.Azure_OpenAI_api_key,
            api_version=self.Azure_OpenAI_api_version)
    
    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
        )
        return response.choices[0].message.content