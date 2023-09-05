# script para graficar un archivo de cvs gnerico
# ******* EN DESARROLLO 4-sep-23 *******

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Configuración del script:

ruta_base = '/home/mariano/Docs-GoogleDrive/Descargas/23_Allegro-UTN/shottky/'
ruta_especifica = 'med_directa_dist_areas_y_dist_temp/6x6_csv/'
nombre_archivo = 'site2.1_tile4_device23_-5to5_0C.csv'
ruta_archivo = ruta_base + ruta_especifica + nombre_archivo

df = pd.read_csv( ruta_archivo )
print(df)

#agregar una columna y2 que sea el abs(i_a) para luego graficar en semilogy

df.plot(x='v_a', y='i_a', logy=True, title=nombre_archivo, marker='o', linestyle='dashed', color='red')
plt.show(block=False)
plt.show()
