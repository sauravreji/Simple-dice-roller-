from PIL import Image
import os

def compressimage(inputpath, outputpath, quality=85):
    try:
       
        with Image.open(inputpath) as img:
           
            img.save(outputpath, 'JPEG', quality=quality)
        print(f"Compression successful! Saved as {outputpath}")
    except Exception as e:
        print(f"Error: {e}")


inputimagepath = 'example.jpg'
outputimagepath = 'example_comressed.jpg'
compressimage(inputimagepath, outputimagepath)
