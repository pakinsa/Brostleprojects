from PIL import Image
from pytesseract import*
import requests
import io



# Prompt the user to enter the image URL
image_url = input("Please enter the URL of the image: ")

# Download the image from the URL
response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))

# Convert the image to text using OCR (Optical Character Recognition)
text = pytesseract.image_to_string(image)

# Save the text to a file
with open("output.txt", "w") as file:
    file.write(text)

print("Image converted to text and saved as 'output.txt'.")

