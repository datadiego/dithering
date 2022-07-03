from PIL import Image, ImageOps
import sys

try:
    img = Image.open("./img/1.jpg")
    img = ImageOps.grayscale(img)

except:
    print("No se pudo cargar la imagen")
    sys.exit(1)

ancho, alto = img.size
pixels = img.load()
threshold = 128
for x in range(0,ancho):
    for y in range (0,alto):
        if pixels[x, y] < threshold:
            new_pixel = 0
            pixels[x, y] = new_pixel 
        else:
            new_pixel = 255
            pixels[x,y] = new_pixel
img.show()
img.save("2.png", "png")