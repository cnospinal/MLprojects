#ORGANIZA ARCHIVOS DE VARIAS CARPETAS EN UNA UNICA CARPETA

import shutil as sht 
import os

carpeta_padre='D:/FOTOS'
carpeta_final='D:/BACKUP FOTOS'

lista=os.listdir(carpeta_padre)

for i in lista:
    carpeta_copia=carpeta_padre+'/'+i
    lista2=os.listdir(carpeta_copia)
    for j in lista2:
        ruta_copia=carpeta_copia+'/'+j
        sht.copy(ruta_copia,carpeta_final)
        print('Archivo copiado',ruta_copia)
