import fitz
from pathlib import Path


IMAGE_OUTPUT_DIR = Path("data/pdf_images")
IMAGE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def extract_images(pdf_path: str):

    pdf = fitz.open(pdf_path)

    pdf_name = Path(pdf_path).stem

    save_dir = IMAGE_OUTPUT_DIR / pdf_name
    save_dir.mkdir(parents=True, exist_ok=True)

    extracted_images = []

    for page_number in range(len(pdf)):

        page = pdf.load_page(page_number)

        images = page.get_images(full=True)

        for image_index, img in enumerate(images):

            xref = img[0]

            base_image = pdf.extract_image(xref)

            image_bytes = base_image["image"]

            extension = base_image["ext"]

            image_name = f"page_{page_number+1}_img_{image_index+1}.{extension}"

            image_path = save_dir / image_name

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            extracted_images.append(
                {
                "page": page_number + 1,
                "image_index": image_index + 1,
                "image_path": str(image_path)
                }
            )

    pdf.close()

    return extracted_images