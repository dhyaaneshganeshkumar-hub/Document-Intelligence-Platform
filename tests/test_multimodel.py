import base64

from langchain_core.messages import HumanMessage

from src.llm.llm import llm


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


image_path = "data/pdf_images/sample_images/page_1_img_1.jpeg"

image_base64 = image_to_base64(image_path)

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Describe this image in detail. If it is a table, graph, diagram or chart explain every important detail."
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{image_base64}"
            },
        },
    ]
)

response = llm.invoke([message])

print(response.content)