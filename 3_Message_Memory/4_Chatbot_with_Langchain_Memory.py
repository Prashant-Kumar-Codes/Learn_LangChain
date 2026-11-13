from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

aiModel = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

messages_memory = [
    SystemMessage(content='You are a helpful assistant which answers each query with paitence and correctness with double check')
]

while True:
    user_input = HumanMessage(content = input('User: '))
    if user_input=='break': break

    messages_memory.append(user_input)

    ai_output = aiModel.invoke(messages_memory)
    print(f'AI: {ai_output.content}')
    messages_memory.append(AIMessage(content=ai_output.content))


print(messages_memory)