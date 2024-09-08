from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 


load_dotenv()

key=os.getenv("GROQ_API_KEY")


model=ChatGroq(model="llama3-8b-8192",temperature=0.0,api_key=key)

response=model.invoke("hello")
print(response)
