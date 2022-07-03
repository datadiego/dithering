from PIL import Image
import random
randint = random.randint
img = Image.new(mode="1", size=(200, 200))
def rgb_noise(img):
    ancho, alto = img.size
    pixels = img.load()
    for x in range(0, ancho):
        for y in range(0, alto):
            rgb = randint(0,254)
            pixels[x, y] = rgb
    img.show()

def greyscale_noise(img):
    ancho, alto = img.size
    pixels = img.load()
    for x in range(0, ancho):
        for y in range(0, alto):
            rgb = randint(0,254)
            pixels[x, y] = rgb
    img.show()

if __name__ == "__main__":
    img = Image.new(mode="L", size=(200, 200))
    rgb_noise(img)
    img2 = Image.new(mode="L", size=(200, 200))
    greyscale_noise(img2)

