# -*- coding: utf-8 -*- 
""" 
Surveille l'arrivee de nouveaux fichiers image dans un repertoire local, 
les traite au fur et a mesure et sauve les images traitees.
option : supprime les images raw (deconseille)
"""

#imports pour chemins d'acces
import os
from pathlib import Path
import time


# imports traitement images
import PIL.ImageOps
from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import SaveAs
import numpy as np
# from skimage import io
# from sklearn.cluster import KMeans



#---------------------------------------------------------------------
def update_list_fic(path, old_list, flag='*'):
    '''
    met a jour la liste de fichiers presents dans un dossier,
    distingue la liste des nouveaux fichiers
    ----------
    path: PATH chemin du dossier
    old_list :  ancienne liste des fichiers
    flag : str. pour selection du nom des fichiers a mettre a jour
    -------
    new_list : liste mise a jour de tous les fichiers (liste d'objets "WindowsPath")
    new_files : liste des nouveaux fichiers
    '''
    p = Path(path)
    new_list = list(p.glob(flag))
    new_files = sorted(list(set(new_list)-set(old_list)))
    return new_list, new_files


#---------------------------------------------------------------------
def resize(path, n):                #donner le fichier a compresser, et le ratio de division de taille
    Image_in = PIL.Image.open(path)
    height, width = Image_in.size
    Image_out = PIL.ImageOps.fit(Image_in, (int(height/(np.sqrt(n))),int(width/(np.sqrt(n)))) )   #divise la taille par n
    return(Image_out)


#---------------------------------------------------------------------
def quantize(image,n):              #provient de wikipedia color quantization > python
    im2 = image.quantize(n)
    return(im2)                     # NON UTILISEE
    
    
 #--------------------------------------------------------------------- 
def saveImg(processed_img,file_path, savedir,my_quality):
    # travaille sur chemin et nom fichier
    head, tail = os.path.split(path)
    final_file_dir = os.path.join(os.path.dirname(head),savedir)
    final_file_name = tail.rsplit('.', maxsplit=1)[0]+"_compressed.JPG"
    final_file_path = os.path.join(final_file_dir,final_file_name)
    # sauvegarde avec PIL 
    processed_img.save(final_file_path, quality=my_quality )
    # echo
    print (final_file_name, "   saved")
    return True



#-----------------------------------------------------------------------------#
if __name__ == '__main__':

    # on testera toutes les t_scrutation secondes si des fichiers sont "arrives"
    t_scrutation = 5     
    # chemin dossier image a traiter
    local_dir_path = "/home/scar/Documents/Programme/img_a_traiter"
    # nom dossier image sauvegarde
    savedir = "img_traitees"
    # on peut selectionner les fichiers a traiter (exemple "*.jpeg")
    flag  = '*.jpg'
    # option suppression des images raw (true / False)
    suppr_raw_img = False
    
    
    #------ COMPRESSION USER MENU ----#
    reduction_factor = 1
    my_quality = 50                  
    #------ COMPRESSION USER MENU ----#
    
    
    #inits
    list_fic = []
    n_fic_tot = 0
    dest_dir_path = os.path.join(os.path.dirname(local_dir_path) , savedir)
    os.makedirs(dest_dir_path, exist_ok=True)


    #-- BOUCLE PRINCIPALE ----------------------------------
    while 1:
            time.sleep(t_scrutation)
            list_fic, new_files = update_list_fic(local_dir_path, list_fic, flag)
            
            if new_files:
                # des nouvelles images ont ete trouvees
                n_fic_tot += len(new_files)
                now = time.localtime()
                # on le signale
                print((time.strftime("%d/%m/%y %H:%M:%S", now)  + 
                       ' -> %s nouveaux fichiers trouves. Total: %s fichiers')%(
                           len(new_files), n_fic_tot))
                
                # on traite les nouvelles images et, si option choisie, on supprime les images raw
                for path in new_files :
                    
                    # 1) redimensionnement
                    img_resized = resize(path, reduction_factor)
                    
                    # 2) color quantization  ...  NON UTILISE
                    # quant_img = quantize(img_resized, 16)   
                    # ne fonctionne pas car convertit l'image en mode RGB vers une image en mode P
                    # les images sont standard RGB-24bits (8x8x8) 8 bit sur chaque canal (16millions de couleurs)
                    # donc on va transformer manuellement les images jpeg "8bits" en images jpeg "1/2/3 ou 4 bits"
                    # en passant par des np array
                    '''
                    eightbitsdata = np.asarray(img_resized)
                    buffer = eightbitsdata / 8
                    lessbitsdata = np.round(buffer)
                    quantized_image = PIL.Image.fromarray(lessbitsdata.astype(np.uint8))
                    '''
                    # mais cela n'a pas beaucoup d'interet car PIL sauvegardera de toute facon en format JPEG standard RGB-24Bits
                    # donc on aura juste des images plus sombres sans avoir un effet important en termes de reduction
                    # du poids des imges
                    
                    # 3) qualite : il est plus interessant de jouer sur la compression pour reduire le poids des images jpeg
                    #  nb: par defaut PIL sauvegarde les jpeg avec quality=75
                    # sauvegarde l'image traitee
                    saveImg(img_resized, path, savedir, my_quality)
                    
                    # 4) eventuellement supprime les images raw
                    if suppr_raw_img:
                        os.remove(path)
                    

                
     