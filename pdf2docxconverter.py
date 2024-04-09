from pdf2docx import Converter

input_path='/content/IsmailResume.pdf'
output_path='/content/Cv.docx'

cv=Converter(input_path)
cv.convert(output_path)
cv.close()