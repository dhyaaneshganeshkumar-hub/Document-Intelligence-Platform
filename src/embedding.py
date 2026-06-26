import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings 

load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint = os.getenv("OPENAI_ENDPOINT"),
    api_key = os.getenv("OPENAI_API_KEY"),
    api_version = os.getenv("OPENAI_API_VERSION"),
    model = os.getenv("OPENAI_MODEL_NAME")
)