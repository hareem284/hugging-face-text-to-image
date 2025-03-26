from config import HF_API_KEY
from PIL import Image
from io import BytesIO
import requests
#
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
def generate_image_from_text(prompt:str):
    
    #putting headers
    print("requesting image......")
    headers={"Authorization":f"Bearer {HF_API_KEY}"}
    #putting payload
    payload={"inputs": prompt}
    #
    response=requests.post(API_URL,headers=headers,json=payload,timeout=30)
    #checking if response was sent 
    if 'image' in response.headers.get('Content-Type', ''):
            image = Image.open(BytesIO(response.content))
            return image
    
  
    

def start():
  #  Main loop for user interaction. Continuously prompts the user for a text description,generates an image via the API, displays it, and offers an option to save the image.

    print("Welcome to the Text-to-Image Generator!")
    print("Type 'exit' to quit the program.\n")
    while True:
        prompt = input("Enter a description for the image you want to generate:\n").strip()
        if prompt.lower() == "exit":
          print("Goodbye!")
          break
        else:
            print("generating image......")
            image =generate_image_from_text(prompt)
            image.show()






if __name__=="__main__":
    start()
