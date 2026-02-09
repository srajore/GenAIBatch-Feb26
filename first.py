

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()



client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="Write a poem on Generative AI in 50 words."
)

print(response.output_text)