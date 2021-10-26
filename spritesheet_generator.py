from PIL import Image
import os
import math

DIR_IMAGES = "images"

# Importar imagens
listDir = os.listdir(DIR_IMAGES)
listImg = []

for dirc in listDir:
    listImg.append(Image.open(DIR_IMAGES + "/" +dirc).convert("RGBA"))

# Calcular tamanho da imagem grande
countSize = math.floor(len(listImg) ** (1/2)) + 1

wid, hei = listImg[0].size

maxWid = countSize * wid
maxHei = countSize * hei

# Criar imagem final
finalImg = Image.new("RGBA", (maxWid, maxHei), (255,255,255,0))

# Adicionar imagens
i = 0
width = 0
height = 0

while i < len(listImg):
    print(i, width, height)
    if (width > countSize-1):
        width = 0
        height = height + 1

    posWidth = listImg[0].width * width
    posHeight = listImg[0].height * height

    # Adicionar imagem i na posição
    finalImg.paste(listImg[i], (posWidth, posHeight))
    
    width = width + 1
    i = i + 1

# Exportar imagem
finalImg.save('final_img.png', "PNG")
print("done")
