import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

# 🔐 Configure API key
genai.configure()

# 🤖 Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# 💬 Generate response
response = model.generate_content(
    "Explain GenAI in simple terms with an example"
)

print(response.text)


