from prompt_manager import PromptManager

from llm import my_llm

#prompt = PromptManager.get_prompt('tutor_v1')

prompt = PromptManager.get_prompt('tutor_v2')

chain = prompt | my_llm


result = chain.invoke({
    'topic': 'quantum computing',
    'level': 'beginner'
})


print(result.content)