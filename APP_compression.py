import PIL
from PIL import Image
from tkinter.filedialog import *

root = Tk()     #fenetre choix fichier
root.lift()     #mettre fenetre choix au 1er plan
root.withdraw() #ne pas afficher la fenetre tkinter

file_path = askopenfilename()

Image = PIL.Image.open(file_path)
height, width = Image.size
Img = Image.resize((int(height/2),int(width/2)), PIL.Image.ANTIALIAS)

#save_path = asksaveasfilename()
#Img.save(save_path[:-4]+"_compressed.jpg")
Img.save(file_path[:-4]+"_compressed.jpg")
print("Compression reussie")