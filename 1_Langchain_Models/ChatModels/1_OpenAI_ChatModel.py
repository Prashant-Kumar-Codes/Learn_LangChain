from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

try: load_dotenv()
except: print('unable load environment variables')

ollm = ChatOpenAI(model='gpt-4o-mini')

result = ollm.invoke('What is the aqi of Mohali now?')
print('Response from OpenAI LLM: ', result)

print(result.content)