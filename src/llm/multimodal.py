import base64
from pathlib import Path

from langchain_core.messages import HumanMessage

from src.llm.llm import llm


def encode_image(image_path: str) -> str:
    """
    Convert an image into base64 so it can be sent to GPT-4o.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def describe_image(image_path: str) -> str:
    """
    Uses GPT-4o Vision to describe an image.
    """

    image_path = Path(image_path)

    image_base64 = encode_image(str(image_path))

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": """
You are analyzing an image extracted from a technical PDF.

Return ONLY valid JSON.

{
"type":"",
"title":"",
"summary":"",
"keywords":[],
"entities":[]
}

Rules:
- If image is a graph explain the trend.
- If table summarize it.
- If flowchart explain workflow.
- If UI explain screen.
- If photograph summarize important objects.
- Keep summary under 100 words.
- Do not return markdown.
""",
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

    return response.content

