from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal, Optional
from pydantic import BaseModel,Field

load_dotenv()

llm_Obj = ChatOpenAI(model='gpt-4')

class reviewStatus(BaseModel):
    summary:Optional[str] = Field(description="Write down the summary of review")
    tone: Literal["pos", "neg"] = Field(description="Write down the sentiment of the review")
    name: Optional[str]= Field(description="Write the name of the reviewer")


strucutred_model = llm_Obj.with_structured_output(reviewStatus)

resp = strucutred_model.invoke("""I bought this Iphone 17 2 months back and it is working perfectly fine and OS is very smooth and camera quality is awesome, but only cons is it's price as it is too costly compared to its competitors and screen size is small compared to other models in same segment
Review By: R Prashanth 
""")
print(f"Response in structured output in pydantic object is : {resp}")

""" from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str = 'chinna'
    id: Optional[int] = 1

new_student = {'name':'RPC','id':'33'}

student = Student(**new_student)

print(student) """