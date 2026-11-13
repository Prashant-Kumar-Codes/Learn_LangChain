from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

chat_history = []

while True:
    user_inupt = input('User: ')
    chat_history.append(user_inupt)
    if user_inupt=='break': break
    ai_output = chatModel.invoke(chat_history)
    print(f'AI: {ai_output.content}\n')
    chat_history.append(ai_output)
    
print(chat_history)