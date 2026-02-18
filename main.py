from prompts.tutor_prompt import tutor_prompt
from prompts.summarizer_prompt import summarizer_prompt
from prompts.classifier_prompt import classifier_prompt
from llm import my_llm

# Tutor Example
prompt = tutor_prompt.format(topic="machine learning", level="beginner")

response = my_llm.invoke(prompt)

print('Tutor Response: \n ', response.content)


#summarization example
prompt = summarizer_prompt.format(text="Machine learning is a fascinating field that enables computers to learn and improve their performance on a task without being explicitly programmed. I'd be happy to explain it in beginner-friendly detail with examples. Machine learning is a subset of artificial intelligence that focuses on developing algorithms and models that allow computers to learn from data and make predictions or decisions based on that data. It involves training a model on a large dataset, allowing it to identify patterns and relationships within the data, and then using that model to make predictions or classifications on new, unseen data. For example, in image recognition, a machine learning model can be trained on a dataset of labeled images (e.g., cats and dogs) and then be able to classify new images as either a cat or a dog based on the patterns it learned during training.")

response = my_llm.invoke(prompt)

print('Summarization Response: \n ', response.content)

#classification example
prompt = classifier_prompt.format(text="Amazon has shipped a Pre-activated phone Samsung S25 ultra 512gb. I purchased on Amazon on 8th Feb and as per Samsung center, phone is activated on 3rd Feb itself. Need Amazon to pay for additional warranty and repair costs.")

response = my_llm.invoke(prompt)

print('Classification Response: \n ', response.content)


#---------------------------------------------------------------------


from prompt_store import get_prompt

from llm import llm

#from langchain_core.messages import HumanMessage

#choose prompt dynamically

PROMPT_VERSION='1'

#fetch prompt from Bedrock

prompt_text = get_prompt(
    'OTS18UJBBH',
    PROMPT_VERSION,
    {
        "topic": "quantum computing",
       #"level": "beginner"
    }
)



#response = llm.invoke(HumanMessage(content=prompt_text))

response = llm.invoke(prompt_text)

print(response.content)