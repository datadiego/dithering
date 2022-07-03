from PIL import Image, ImageOps
import sys

def error_dithering(img_path, threshold, sav):
    try:
        img = Image.open(img_path)
        img = ImageOps.grayscale(img)
    except:
        print("No se pudo cargar la imagen")
        sys.exit(1)

    ancho, alto = img.size
    pixels = img.load()
    error = 0
    for x in range(0,ancho):
        for y in range (0,alto):
            pixels[x,y] += error
            if pixels[x, y] < threshold:
                new_pixel = 0
                error = pixels[x,y]
                pixels[x, y] = new_pixel
            else:
                new_pixel = 255
                error = pixels[x,y]-255
                pixels[x,y] = new_pixel
    
    if sav == True:
        img.save("2.png", "png")
        img.show()
    else:
        img.show()


if __name__ == "__main__":
    path_og = "1a.jpg"
    a = error_dithering(path_og, 128, True)
