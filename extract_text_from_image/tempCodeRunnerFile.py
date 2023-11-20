import pytesseract
from PIL import Image
value=Image.open('logo.png')
text=pytesseract.image_to_string(value)
print("Extracted Data is: \n ", text)