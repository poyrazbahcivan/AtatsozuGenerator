from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import random
import shutil

#RandomImage
imgExtension = ["png", "jpeg", "jpg"]
allImages = list()
def chooseRandomImage(directory="./photos/"):
    for img in os.listdir(directory):
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice]
    return "./photos/" + chosenImage
text = input('Atatsozu girin: ')
text = text + "\n" + "-Mustafa Kemal Ataturk"
randomImage = chooseRandomImage()
print(randomImage)

#WriteOver
output = '.atasozlu.jpg'
img = Image.open(randomImage)
d = ImageDraw.Draw(img)
width,height = img.size
fontsize = img.size[0]/150*13 #Font boyutunu resim boyutuna gore hesapla 
font = ImageFont.truetype("impact.ttf",(int)(fontsize)) #Fontu ayarla
w,h = d.textsize(text,font) # Fontla birlikte yazinin boyutu
while w>width: # Tasma kontrol
    fontsize = fontsize-1
    font = ImageFont.truetype("impact.ttf",(int)(fontsize)) #Fontu ayarla
    w,h = d.textsize(text,font) # Fontla birlikte yazinin boyutu

d.text(((width-w)/2,(height-h)/1.4),text,'white',font) #Yaziyi yaz
img.save('atatsozu.png')
print(width,height)
print(fontsize)