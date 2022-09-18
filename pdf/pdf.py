import pdfminer.high_level

with open('pdfTest.pdf', 'rb') as file:
    file1 = open(r'pdfText.txt', 'a+')
    pdfminer.high_level.extract_text_to_fp(file, file1)
    file1.close()