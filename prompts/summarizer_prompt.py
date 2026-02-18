from langchain_core.prompts import PromptTemplate

summarizer_prompt = PromptTemplate(
    template="Summarize the following text in 3 bullet points: {text}",
    input_variables=["text"]
)