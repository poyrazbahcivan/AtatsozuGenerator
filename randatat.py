from cgitb import text
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
randomImage = chooseRandomImage()
print(randomImage)

#RandomSozler
def randnum(fnum):
	lines=open(fnum).read().splitlines()
	return random.choice(lines)
text = randnum('sozler.txt')
print(text)
text = list(text)
text.insert((int)(len(text)/2), '\n')
text = ''.join(text)
text = text + "\n" + "-Mustafa Kemal Ataturk"
print(text)
#WriteOver
output = '.atasozlu.jpg'
img = Image.open(randomImage)
d = ImageDraw.Draw(img)
width,height = img.size
fontsize = img.size[0]/150*10 #Font boyutunu resim boyutuna gore hesapla 
font = ImageFont.truetype("impact.ttf",(int)(fontsize)) #Fontu ayarla
w,h = d.textsize(text,font) # Fontla birlikte yazinin boyutu
while w>width: # Tasma kontrol
    fontsize = fontsize-1
    font = ImageFont.truetype("impact.ttf",(int)(fontsize)) #Fontu ayarla
    w,h = d.textsize(text,font) # Fontla birlikte yazinin boyutu

d.text(((width-w)/2,(height-h)/2),text,'white',font) #Yaziyi yaz
img.save('atatsozu.png')
print(width,height)
print(fontsize)
img.show()

#Twitter API eklenecek.