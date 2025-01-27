import os
from pathlib import Path
from pypdf import PdfReader
from pdfly.up2 import up2_main

# Create a simple 6-page blank PDF for testing
def create_test_pdf(file_path, num_pages=6):
    from pypdf import PdfWriter
    writer = PdfWriter()
    for _ in range(num_pages):
        writer.add_blank_page(width=210, height=297)  # A4 size in mm
    with open(file_path, "wb") as f:
        writer.write(f)

# File paths for the input and output PDFs
input_pdf = Path("test_input.pdf")
output_pdf = Path("test_output.pdf")

# Create the test PDF
create_test_pdf(input_pdf)

# List of layouts to test
layouts = ["2x2", "3x3", "1x2", "2x1"]
for layout in layouts:
    print(f"\nTesting layout: {layout}")
    up2_main(input_pdf, output_pdf, layout=layout)
    
    # Read the output PDF and print the number of pages
    reader = PdfReader(str(output_pdf))
    print(f"Output PDF for layout {layout} has {len(reader.pages)} pages.")

# Clean up
if output_pdf.exists():
    os.remove(output_pdf)
if input_pdf.exists():
    os.remove(input_pdf)
