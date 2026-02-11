from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

response = llm.invoke("Tell me the key achivements of Virat Kohli in 3 bullet points.")
print(response.content)