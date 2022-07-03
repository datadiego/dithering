from PIL import Image, ImageOps
import sys
from random import randint

def down_white_pixels(img_path, sav):
    try:
        img = Image.open(img_path)
        img = ImageOps.grayscale(img)
    except:
        print("No se pudo cargar la imagen")
        sys.exit(1)

    ancho, alto = img.size
    pixels = img.load()
    
    for x in range(0, ancho):
        for y in range(alto-2, -1, -1):
            val = randint(0,4)
            if pixels[x,y] == 255 and pixels[x,y+1] == 0:
                pixels[x,y] = 0
                pixels[x,y+1] = 255
            if pixels[x,y] == 255 and pixels[x,y+1] == 255:
                pixels[x,y] = 255
                pixels[x,y+1] = 255
    
            
    
    img.save(sav, "png")
    


if __name__ == "__main__":
    path_og = "/0.png"
    for i in range(0, 320):
        path_og = str(i)+".png" #Empezamos con el archivo 0
        a = down_white_pixels(path_og, str(i+1)+".png") #Creamos el siguiente frame y lo salvamos
        print("Imagen "+str(i)+ " creada")
