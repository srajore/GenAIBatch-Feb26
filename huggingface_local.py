import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ⭐ Small local model
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer + model locally (downloads first time only)
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,   # change to float16 if GPU
    device_map="auto"
)

# Create HF pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.5,
    do_sample=True,
)

# Wrap pipeline for LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Prompt template (same structure as yours)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

# Chain
chain = prompt | llm | StrOutputParser()

# Run
response = chain.invoke({
    "question": "Who is Mahatma Gandhi?"
})

print(response)