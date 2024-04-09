import pdfplumber as pp

page_number=0;
text=''
output_txt_path = "output.txt"

with pp.open('resume.pdf') as pdf:
    page=pdf.pages[page_number]
    text=page.extract_text()

with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
  txt_file.write(text)

