import cv2
import re
import pytesseract


img = cv2.imread('photo_2022-07-18_11-51-21.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 3 --psm 13'
result = pytesseract.image_to_string(img, config=custom_config)
result_number = re.findall(r'\d', result)
print(result_number)



