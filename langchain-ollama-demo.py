from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi4-mini:latest"
)

response = llm.invoke("Tell me the key achivements of Virat Kohli in 3 bullet points.")
print(response.content)