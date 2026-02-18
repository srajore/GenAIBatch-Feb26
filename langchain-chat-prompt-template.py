from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt  = ChatPromptTemplate.from_messages([
   ("system", "You are a helpful AI assistant that provides information about the achievements of famous personalities."),
   ("human", "Tell me the key achievements of {name} in {num_points} bullet points."),
])




llm = ChatOllama(
    model="phi4-mini:latest"
)

chain= prompt | llm   #LCEL

username = input("Whose achivements you would like to know ? Press Enter to continue...")

response = chain.invoke({"name": username, "num_points": 2})

#response = llm.invoke(prompt.format(name="Mahatma Gandhi"))


print(response.content)