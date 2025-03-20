from PIL import Image
import pytesseract

# If Tesseract is not in your PATH, specify its installation location
# Example for Windows (adjust the path if necessary)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image using Pillow
image = Image.open('a02-116.png')

# Use pytesseract to do OCR on the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text: ", extracted_text)


import cv2
import pytesseract

# Load the image
image = cv2.imread('a02-116.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Optionally, apply thresholding to binarize the image
_, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

# Use pytesseract to extract text
extracted_text = pytesseract.image_to_string(thresholded_image)

print("Extracted Text: ", extracted_text)


# Save the extracted text to a file
with open('extracted_text.txt', 'w') as file:
    file.write(extracted_text)

# Or print it directly
print(extracted_text)
