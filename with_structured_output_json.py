from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

llm_obj = ChatOpenAI(model='gpt-4')

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "tone": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["summary", "tone"]
}


structured_model = llm_obj.with_structured_output(json_schema)

result = structured_model.invoke("""I bought this Iphone 17 2 months back and it is working perfectly fine and OS is very smooth and camera quality is awesome, but only cons is it's price as it is too costly compared to its competitors and screen size is small compared to other models in same segment
Review By: R Prashanth Chowdary Posted on : 23.05.2025
""")

print(f"Structured output in json format is : {result}")