'''
pip install PyPDF2 -
pip install fpdf
'''

import PyPDF2
 
# Open sample pdf to replace text in pdf
pdf_file = PyPDF2.PdfReader(open("filename.pdf", "rb"))

prtint(pdf_file.metadata)
# Count number of pages in our pdf file
number_of_pages = len(pdf_file.pages)
# print number of pages in the pdf file
print("Number of pages in this pdf: " + str(number_of_pages))

# Read first page
page = pdf_file.pages[0]
 
# print entire text of first page of the pdf
text = page.extract_text()
print(text)

print(page.mediabox.width, page.mediabox.height)

old_text = "old text"
new_text = "new text"
 
# Read first page
page = pdf_file.pages[0]
text = page.extract_text()
 
# replace text in pdf
text = text.replace(old_text, new_text)
print(text)


'''
save the edited file to PDF
'''

from fpdf import FPDF
 
# Create PDF object
pdf = FPDF()
 
# Read text file
text2 = text.encode('utf-8').decode('latin-1')
 
# Split text into pages
lines_per_page = 4000
text_pages = [text2[i:i+lines_per_page] for i in range(0, len(text2), lines_per_page)]
 
# Write text pages to PDF
pdf.set_font("Arial", size=12)
for text_page in text_pages:
    pdf.add_page()
    pdf.multi_cell(200, 10, txt=text_page, align="L")
 
# Save PDF
pdf.output("output_file.pdf", "F")
