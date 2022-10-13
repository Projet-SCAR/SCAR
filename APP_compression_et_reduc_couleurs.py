#mettre ds la commande : pip install pillow
import PIL
from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import SaveAs

import numpy as np
from skimage import io
from sklearn.cluster import KMeans


#root = Tk()     #fenetre choix fichier
#root.lift()     #mettre fenetre choix au 1er plan
#root.withdraw() #ne pas afficher la fenetre tkinter

def openImg #transforme path ennp
#A FAIRE

def resize(path, n):
    Image1 = PIL.Image.open(path)
    height, width = Image1.size
    Image1.resize((int(height/(n/2)),int(width/(n/2))), PIL.Image.ANTIALIAS)  #divise la taille par 4
    
    return(np.array(Image1))


#def reduc_RGB(image,n):
#      #result = image.convert('P', palette=Image.ADAPTIVE, colors=n)  
#      #/!\ prochaine fois : explorer image.quantize
#    original = image
#    n_colors = 6
#    
#    arr = original.reshape((-1, 3))
#    kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(arr)
#    labels = kmeans.labels_
#    centers = kmeans.cluster_centers_
#    less_colors = centers[labels].reshape(original.shape).astype('uint8')
#    
#    #io.imshow(less_colors)
#    return(less_colors)
#    

def quantize(image,n):       #☻provient de wikipedia color quantization > python
    im = Image.open("frog.png")
	im2 = im.quantize(n)
	im2.show() 
    return(im2)
    
    
      

def SaveImg:
    #A FAIRE
    
    
    
file_path = askopenfilename()

img_resized=resize(file_path, 4) #donner le fichier a compresser, et le ratio de division de taille

final_img=reduc_RGB(img_resized, 128)

#save_path = asksaveasfilename()             
#Img.save(save_path[:-4]+"_compressed.jpg")

final_img.SaveAs(file_path[:-4]+"_compressed.jpg")
print("Compression reussie")