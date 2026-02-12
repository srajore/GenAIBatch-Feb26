from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
)

response = model.invoke("What are the key achievements of Rohit Sharma in 3 bullet points?") 
print(response.content)