from typing import Union
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import List


load_dotenv()


class SquizItem(BaseModel):
    question:str=Field(description="""
    The open-ended qestion related to the context in format 1.question_content...\n
    """)

class SquizList(BaseModel):
    squiz_list:List[SquizItem]=Field(description="""A complete squiz with open-ended questions.""")

    
class GenerateQuiz:
    def __init__(self):
        self.model_name="llama3-8b-8192"
        self.model_temperature=0.0
        
    def __init_model(self):
        try:
            model = ChatGroq(name=self.model_name,temperature=self.model_temperature,api_key=os.getenv("GROQ_API_KEY"))
            return model
        except Exception as e:
            return e
    def generate_respose(self,query:str,img_to_txt:str):
        try:
            model=self.__init_model()
            model.with_structured_output(SquizList)
            prompt = PromptTemplate(template="""
            You're primary task is analize the context provided bellow and generate an quiz with at least 3 open-ended questions and a maximum of 10\n
            Important don't include teh response only the question.                        
            Optionally you can follow another request if teh query provided by the user exists
                                    
            This is the context\n:
            {context}

            This is the query:
            {query}                        
            
                                    """,input_variables=["query","context"])
            chain_squiz=prompt|model
            response=chain_squiz.invoke({"query":query,"context":img_to_txt})
            return response.content.split("\n")
        except Exception as e:
            return e
        
        
        