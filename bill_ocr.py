""" Program to extract data from bill using Google Cloud Vision API
"""

import requests

from img_base64 import image_to_base64

PROJECT_ID = "qwiklabs-gcp-04-5ef3a2a98ba7"
API_KEY = "AIzaSyBb7xe0Cx7yeVYayS4-6yTq2lL-qRVKYJI"

url = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY

data = {
    "requests": [
        {
            "image": {"content": image_to_base64(r"C:\Users\Harshit Music\Pictures\ticket-5.jpg")},  # type: ignore
            "features": [{"type": "TEXT_DETECTION"}],
        }
    ]
}

head = {
    "Content-Type": "application/json; charset=utf-8",
    "x-goog-user-project": PROJECT_ID
}

response = requests.post(url=url, json=data)

with open(file='out-5.json', mode='w', encoding='utf-8') as file:
    file.write(response.text)
