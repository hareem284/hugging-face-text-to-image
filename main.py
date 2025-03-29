from config import HF_API_KEY
from PIL import Image,ImageEnhance,ImageFilter
from io import BytesIO
import requests
#
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
#defining post processing image
def post_procesing_image(image):
    #increasing the brightness
    b_IMAGE=ImageEnhance.Brightness(image).enhance(1.2)#1.2 means 20% increase in brightness
    c_image=ImageEnhance.Contrast(b_IMAGE).enhance(1.3)#1.3 means 30%
    g_blur_image=c_image.filter(ImageFilter.GaussianBlur(radius=2))
    return g_blur_image

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
    else:
        print("Could not get an image")
        return None
#making a starting function
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
            if image!=  None:
              image.show()
              print("applying post procssesing effects")
              p_image=post_procesing_image(image)
              p_image.show()
              save=input("do you want to save the image").strip().lower()
              if save=="yes":
                  f_name=input("please tell the file name which it should be saved in")
                  p_image.save(f"{f_name}.png")

            else:
              break






if __name__=="__main__":
    start()
