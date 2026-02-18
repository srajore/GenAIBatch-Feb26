from langchain_aws import ChatBedrockConverse
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

prompt  = PromptTemplate(
    template="Tell me the key achivements of {name} in 3 bullet points.",
    input_variables=["name"]
)

llm = ChatBedrockConverse(
    model_id="anthropic.claude-3-haiku-20240307-v1:0"
)


chain= prompt | llm   #LCEL

username = input("Whose achivements you would like to know ? Press Enter to continue...")

response = chain.invoke({"name": username})

#response = llm.invoke(prompt.format(name="Mahatma Gandhi"))


print(response.content)










