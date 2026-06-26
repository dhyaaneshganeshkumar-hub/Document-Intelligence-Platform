from src.llm import llm

responce = llm.invoke("what is CAN FD?")

print(responce.content)