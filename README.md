#Structured Outputs in Langchain

#Concepts covered
1) When we send prompts to LLMs, they respond back in textual format i.e., in unstrucutred data
2) This unstructured data we can't use it to call/send to other applications (like API's , database etc..)
3) Therefore in multi environment where one AI agent needs to talk to another agent, they need to communicate using structured data
4) Strucutred data can be in json format or pydantic object format or typeddict format
5) Basically there are 2 types of LLMs , one is where they have capability to return response in structured output, because they might be fine tuned in such a way that if user wants response in some format they can do it
   and other form is LLMs where they cant generate output in structured output, here in this case we can use "output parsers" to convert response into structured output
6) For the LLMs which have capability to return response in structured format, we have method called with_structured_Output" in Langchain through which we can get response in
   structured format (json, pydantic , typeddict)

#Technologies/modules used
1) Python
2) Langchain
3) ChatOpenAI
4) pydantic
5) typing (for typeddict, Optional)
