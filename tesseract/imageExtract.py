from PIL import Image
from pytesseract import pytesseract

tesseract_path = '/usr/bin/tesseract'
image_path = './script.jpeg'
pytesseract.tesseract_cmd = tesseract_path
img = Image.open(image_path)

text = pytesseract.image_to_string(img)

print(text[:-1])
