from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter, PageObject

# Paths
input_path = "Dream Life Journal 2025 2.pdf"
output_path = "Resized_Dream_Life_Journal.pdf"

# Desired dimensions in pixels
new_width_px = 1530
new_height_px = 1933

# Convert PDF pages to images
images = convert_from_path(input_path, dpi=300)

# Resize each image and save to a new PDF
writer = PdfWriter()
for img in images:
    # Resize the image
    img_resized = img.resize((new_width_px, new_height_px), Image.ANTIALIAS)

    # Save the resized image to a temporary PDF
    temp_path = "temp_page.pdf"
    img_resized.save(temp_path, "PDF")

    # Add the resized page to the new PDF
    with open(temp_path, "rb") as temp_file:
        writer.add_page(PdfReader(temp_file).pages[0])

# Save the final resized PDF
with open(output_path, "wb") as output_file:
    writer.write(output_file)

print("PDF resized successfully!")

