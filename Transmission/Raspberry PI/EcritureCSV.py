#!/usr/bin/python
""" Ce code n'es pas utilisé, il l'étais pour l'expérimentation de l'écriture de donnée sous format csv"""
import csv
import smbus
import time
import struct
bus = smbus.SMBus(1)
time.sleep(1)
address = 0x8
d = open('data.csv','w',newline='')
w = csv.writer(d)
while True:
    try:
        L = bus.read_i2c_block_data(address,0,12)
        templ = []
        huml = []
        luml = []
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
        Li = [round(temp,1),round(hum,1),round(lum),time.ctime()]
    except:
#         import pdb
#         pdb.set-trace()
        Li=['Nan','NaN','NaN',time.ctime()]
    print(Li)
    w.writerow(Li)
    d.flush()
    time.sleep(1);
