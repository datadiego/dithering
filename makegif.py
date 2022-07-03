import PIL
from PIL import Image

imagenes = []
for i in range(320,0, -1):
    imagenes.append(Image.open(str(i)+".png"))
for i in range(0,320):
    imagenes.append(Image.open(str(i)+".png"))
ancho, alto = imagenes[0].size
imagen=Image.new(mode="RGB", size=(ancho,alto))
imagen.save("out0.gif", save_all=True, append_images=imagenes)