from src.ingestion.image_ingestion import process_pdf_images

images = process_pdf_images("data/sample_files/sample_images.pdf")

for img in images:
    print("="* 80)
    print(img)