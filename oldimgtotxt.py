from PIL import Image
import pytesseract

# Open the image file
img = Image.open('image.png')

# Convert the image to text
text = pytesseract.image_to_string(img)

# Print the text
print(text)
