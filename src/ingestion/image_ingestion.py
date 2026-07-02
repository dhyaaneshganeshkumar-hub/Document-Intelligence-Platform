from src.vision.vision_processor import extract_images
from src.llm.multimodal import describe_image


def process_pdf_images(pdf_path: str):

    images = extract_images(pdf_path)

    processed_images = []

    for image in images:

        description = describe_image(image["image_path"])

        processed_images.append(
            {
                "page": image["page"],
                "image_index": image["image_index"],
                "image_path": image["image_path"],
                "description": description,
            }
        )

    return processed_images