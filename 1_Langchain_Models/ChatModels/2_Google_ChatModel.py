from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
result = model.invoke('Write a poem on laptop within 5 lines.')

print(f'Result from the chat model:\n{result}')

print(f'\n\nResult content:\n{result.content}')