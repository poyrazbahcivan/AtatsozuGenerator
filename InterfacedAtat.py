from turtle import right
import PIL.Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import random
import shutil
import tkinter as tk
from tkinter import *

top = tk.Tk()
def Apply():
    global E1
    text = E1.get()
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
    text = text + "\n" + "-Mustafa Kemal Ataturk"
    randomImage = chooseRandomImage()
    print(randomImage)

    #WriteOver
    output = '.atasozlu.jpg'
    img = PIL.Image.open(randomImage)
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
    img.show()
top.title('Atatsozu')
applyButton = tk.Button(top, text ="Apply", command = Apply)
applyButton.pack(side=RIGHT)
L1 = Label(top, text="Atatsozu gir:")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)








top.mainloop()