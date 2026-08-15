
import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
load_dotenv()


class ChatGPTHandler:
    """Handler for OpenAI ChatGPT interactions."""

    def __init__(self, model_name: str = "gpt-5.6-luna"):
        self.model_name = model_name
        #self.model_name =  "gpt-5.6-luna"
        self.api_key = os.getenv("CHAT_GPT_API")

        if not self.api_key:
            raise ValueError("CHAT_GPT_API environment variable is not set.")

        self.client = OpenAI(api_key=self.api_key)
        self.llm = ChatOpenAI(
                model=model_name,
                api_key=self.api_key,
                temperature=0,
                reasoning_effort="none" 
                
            )
    
    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
        )
        return response.choices[0].message.content
