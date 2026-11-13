from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

while True:
    user_input = input('User: ')
    if user_input == 'break':
        break
    ai_output = chatModel.invoke(user_input)
    print(f'Ai: {ai_output.content}\n')