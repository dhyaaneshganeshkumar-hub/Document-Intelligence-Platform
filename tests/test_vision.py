from src.vision.vision_processor import extract_images

images = extract_images("data/sample_files/sample_images.pdf")

for image in images:
    print(images)
    