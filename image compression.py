import numpy as np 
import requests
import cv2
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


img = Image.open('original.jpg')

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def getprompt(img):
    print("getting prompt")
    inputs = processor(img, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption


def decompress(prompt):
    print("getting image")
    url = "https://image.pollinations.ai/prompt/"
    response = requests.get(url + prompt)

    with open('generated.png', 'wb') as f:
        f.write(response.content)

    generated = cv2.imread('generated.png')
    cv2.imwrite("generated.png", generated)
    generated = generated[45:-45, 45:-45]
    cv2.imshow("generated", generated)
    cv2.waitKey(0)


prompt = getprompt(img)
print(prompt)
decompress(prompt)