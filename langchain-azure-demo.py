from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


prompt  = PromptTemplate(
    template="Tell me the key achivements of {name} in 3 bullet points.",
    input_variables=["name"]
)

llm = AzureChatOpenAI(
    azure_deployment="gpt-4.1",  # or your deployment
    api_version="2024-12-01-preview",  # or your api version
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

chain= prompt | llm   #LCEL

username = input("Whose achivements you would like to know ? Press Enter to continue...")

response = chain.invoke({"name": username})

print(response.content)