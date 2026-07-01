import json

from langchain_core.prompts import ChatPromptTemplate
from src.llm.llm import llm

prompt = ChatPromptTemplate.from_template("""
Extract ONLY the important named entities from the question.

Rules:
- Return ONLY a JSON array.
- Keep complete names together.
- Do not include question words.

Examples:

Question:
Who is John Galt?

Output:
["John Galt"]

Question:
Explain AUTOSAR COM Stack

Output:
["AUTOSAR COM Stack"]

Question:
{question}
""")

chain = prompt | llm


def extract_entities(question: str):
    try:
        response = chain.invoke({"question": question})
        return json.loads(response.content)
    except Exception as e:
        print("Entity extraction failed:", e)
        return []
    
if __name__ == "__main__":
    print(extract_entities("Who is John Galt?"))
    print(extract_entities("Explain AUTOSAR COM Stack"))