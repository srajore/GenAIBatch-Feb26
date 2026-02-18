from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_aws.chat_models import ChatBedrockConverse

my_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

llm = ChatBedrockConverse(
    model='anthropic.claude-3-haiku-20240307-v1:0',
    region_name='ap-south-1',
    temperature=0.3,
)