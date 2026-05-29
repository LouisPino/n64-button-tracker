import os
from PyPDF2 import PdfMerger

# Define the paths for the "combine" folder and the output PDF
desktop_path = os.path.expanduser("~/Desktop")
combine_folder = os.path.join(desktop_path, "combine")
output_file = os.path.join(desktop_path, "combined.pdf")

# Create a PDF merger object
merger = PdfMerger()

# Loop through all the PDF files in the combine folder
for filename in sorted(os.listdir(combine_folder)):
    if filename.endswith(".pdf"):
        file_path = os.path.join(combine_folder, filename)
        # Append each PDF to the merger
        merger.append(file_path)

# Write the combined PDF to the output file
with open(output_file, "wb") as output_pdf:
    merger.write(output_pdf)

# Close the merger
merger.close()

print(f"Combined PDF saved as {output_file}")
