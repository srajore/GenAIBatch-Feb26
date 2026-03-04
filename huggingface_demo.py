import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Step 1 — create HF endpoint LLM
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    huggingfacehub_api_token=hf_token,
    #max_new_tokens=128,
    #model_kwargs={"temperature": 0.5}
)

# Step 2 — wrap in chat model
chat_model = ChatHuggingFace(llm=llm)

# Step 3 — prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chain = prompt | chat_model

response = chain.invoke({
    "question": "Who won the FIFA World Cup in 1994?"
})

print(response.content)