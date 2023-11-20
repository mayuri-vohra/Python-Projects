import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
value=Image.open('logo.png')
text=pytesseract.image_to_string(value)
print("Extracted Data is: \n ", text)