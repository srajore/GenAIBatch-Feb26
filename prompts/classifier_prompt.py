from langchain_core.prompts import PromptTemplate

classifier_prompt = PromptTemplate(
    template="Classify the sentiment of the test as positive, negative, or neutral: {text}",
    input_variables=["text"]
)