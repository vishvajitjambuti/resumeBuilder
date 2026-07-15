from llmHandler.AzureLLMHandler import AzureLLMHandler
from llmHandler.ChatGptLLMHandler import ChatGPTHandler

def azur():
    llm = AzureLLMHandler("gpt-4.1")
    cleint = llm.client

    llm_client_response = llm.client.chat.completions.create(
        model="gpt-4.1",

        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Give me a short test response."}
        ]
    )


    print("Test response from Azure OpenAI:", llm_client_response.choices[0].message.content)

def chatgpt():
    llm = ChatGPTHandler("gpt-4.1")
    cleint = llm.client

    llm_client_response = llm.client.chat.completions.create(
        model="gpt-4.1",

        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Give me a short test response."}
        ]
    )


    print("Test response from ChatGPT:", llm_client_response.choices[0].message.content)

chatgpt()
