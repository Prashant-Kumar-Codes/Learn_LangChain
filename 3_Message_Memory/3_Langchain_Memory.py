from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

aiModel = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

messages=[
    SystemMessage(content='You are a helpful assistant which answers each query with paitence and correctness with double check'),
    HumanMessage(content='Tell me what is a river?')
]

ai_output = aiModel.invoke(messages)

messages.append(AIMessage(content=ai_output.content))

print(messages)