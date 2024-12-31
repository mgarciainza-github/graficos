# script para graficar un archivo de cvs gnerico

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración del script:

ruta_base = "/home/mariano/Docs-GoogleDrive/Nanolab"
ruta_especifica = "/mediciones/"
nombre_archivo = "IV_sin_plot.csv"
ruta_completa_archivo = ruta_base + ruta_especifica + nombre_archivo

df = pd.read_csv( ruta_completa_archivo )
#print(df)

'''
# Caso 1: generico sin tags
# columna1->x, columna 2->y
plt.plot(df.loc[:,0], df.loc[:,1], marker='s')
#plt.show(block=False)
plt.show()
'''

#Caso 2: IV SMU Nanolab sin 
# columna1->VGS->vdata1A25, columna 2->Id->idata1B25
VGS='vdata1A25'
ID='idata1B26'
plt.plot(df.loc[:,VGS], df.loc[:,ID], marker='s')
plt.show()
