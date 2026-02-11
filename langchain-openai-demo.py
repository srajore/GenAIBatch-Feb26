from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

client = ChatOpenAI(
    model="gpt-5-nano",
)

response = client.invoke("Tell me the key achivements of Virat Kohli in 3 bullet points.")

print(response.content)