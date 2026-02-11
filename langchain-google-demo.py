from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

response = model.invoke("Tell me the key achivements of Virat Kohli in 3 bullet points.")

print(response.content)