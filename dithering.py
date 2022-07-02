from PIL import Image, ImageOps
import sys

def diffusion_error_dithering(img_path, threshold):
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
    img.show()


if __name__ == "__main__":
    path_og = "./img/a.png"
    a = diffusion_error_dithering(path_og, 128)

#img.save("2.png", "png")