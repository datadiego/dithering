from PIL import Image

try:
    img = Image.open("./img/a.png")
    ancho, alto = img.size
    print(f"El ancho de la imagen es: {ancho}")
    print(f"El alto de la imagen es: {alto}")
    img.show()

except:
    print("No se pudo cargar la imagen")

