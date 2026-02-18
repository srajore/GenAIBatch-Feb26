from langchain_core.prompts import ChatPromptTemplate

tutor_prompt = ChatPromptTemplate.from_messages([
    ('system', "You are a expert AI Tutor"),
    ('human', "Explain {topic} in simple word")
])
