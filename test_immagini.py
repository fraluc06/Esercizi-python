import images
Pixel = tuple[int,int,int]

Line = list[Pixel]
Picture = list[Line]


# con valori tra 0 e 255 compresi (1 byte)
# definiamo qualche colore
black : Pixel = 0, 0, 0 # luminosità minime
white : Pixel = 255, 255, 255 # luminosità massime
red : Pixel = 255, 0, 0
green : Pixel = 0, 255, 0
blue : Pixel = 0, 0, 255
cyan : Pixel = 0, 255, 255
yellow: Pixel = 255, 255, 0
purple: Pixel = 255, 0, 255
grey : Pixel = 128, 128, 128


img3 = images.load("3cime.png")


# DEF IMMAGINE TRAMITE LIST COMPREHENSION:

def creaImmagine(altezza: int,larghezza: int,colore: Pixel=black)->list[list[Pixel]]:
  return [[colore]*larghezza for x in range(altezza)] #VENGONO CREATE NUOVE LISTE

# DEF IMMAGINE SENZA LIST COMPREHENSION:

def gen_immagine(altezza: int, larghezza:int, colore: Pixel)->Picture:
    img = []
    for y in range(altezza):
        riga = []
        for x in range(larghezza):
            riga.append(colore)
        img.append(riga)
    return img
    

img1= gen_immagine(200, 200, (0,0,0))
images.visd(img1)
# img=creaImmagine(500, 500, (255,0,255))
# # img[0][50]=(255,0,0)
# images.visd(img)


# images.visd(img3)

import matplotlib.pyplot as plt
import numpy as np
# Per visualizzare ò'immagine in PyCharm
img1_array = np.array(img1, dtype=np.uint8)
plt.imshow(img1_array)
plt.axis('off')
plt.show()