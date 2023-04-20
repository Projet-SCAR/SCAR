#!/usr/bin/python
import csv   # On importe les bibliothèque dont nous avons besoin ^^
import smbus   # On importe les bibliothèque dont nous avons besoin ^^
import time   # On importe les bibliothèque dont nous avons besoin ^^
import struct   # On importe les bibliothèque dont nous avons besoin ^^
import serial   # On importe les bibliothèque dont nous avons besoin ^^
ser=serial.Serial('/dev/ttyS0',9600) # On configure la liaison serie >< *crazy*
ser.timeout = 5
bus = smbus.SMBus(1)
time.sleep(1)
address = 0x8
d = open('data.csv','w',newline='')
w = csv.writer(d)
while True:  #Boucle infinie (true = vrai, while = tant que -> tant que vrai -> tout le temps quoi :p)
    try: #S'il n'y a pas de problème dans la liaison
        L = bus.read_i2c_block_data(address,0,12)
        #Création des listes qui vont recevoir les données
        templ = []
        huml = []
        luml = []
        #byte --> float pour les 3 valeurs
        for i in range(0, 4):
            templ.append(L[i])
        tempb = bytearray(templ)
        temp = struct.unpack('<f',tempb[0:4])
        temp = temp[0] 
        for i in range(4,8): 
            huml.append(L[i])
        humb = bytearray(huml)
        hum = struct.unpack('<f',humb[0:4])
        hum = hum[0]
        for i in range(8,12):
            luml.append(L[i])
        lumb = bytearray(luml)
        lum = struct.unpack('<f',lumb[0:4])
        lum = lum[0]
        # Lister et arrondir /shrug, aussi on date les valeurs
        Li = [round(temp,1),round(hum,1),round(lum),time.ctime()]
    except:
        #S'il il n'il y arrive pas on enregistre sans valeur (NaN = Not a Number)
        Li=['NaN','NaN','NaN',time.ctime()]
    try:
        #transfer de la liste e valeurs par module LoRa
        ser.write(bytes(str(Li)+"\n","utf-8"))
    except:
        #lire plus haut
        ser.write(b'NaN')
    #ecriture csv
    w.writerow(Li)
    d.flush()
    time.sleep(1);
