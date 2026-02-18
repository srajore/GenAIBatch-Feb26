from langchain_core.prompts import ChatPromptTemplate

tutor_prompt = ChatPromptTemplate.from_messages([
    ('system', "You are a senior  AI Tutor. Give examples"),
    ('human', "Explain {topic} for {level} audience with examples")
])