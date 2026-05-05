from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

llm_Obj = ChatOpenAI(model='gpt-4')

class reviewStatus(TypedDict):
    summary:Annotated[Optional[str], "Write down the summary of review"]
    tone: Annotated[Optional[str], "Write down the sentiment of the review"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


strucutred_model = llm_Obj.with_structured_output(reviewStatus)

resp = strucutred_model.invoke("""I bought this Iphone 17 2 months back and it is working perfectly fine and OS is very smooth and camera quality is awesome, but only cons is it's price as it is too costly compared to its competitors
Review By: R Prashanth 
""")
print(f"Response in structured output is : {resp}")