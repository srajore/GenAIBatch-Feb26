

from openai import OpenAI

client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-5-mini",
    input="Write a poem on Generative AI in 50 words."
)

print(response.output_text)