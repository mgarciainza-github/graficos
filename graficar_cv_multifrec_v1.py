# script para graficar un archivo de csv obtenido de mediciones CV multifrec en Nanolab 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Configuración del script:
ruta_base = "/home/mariano/Docs-GoogleDrive/Nanolab/mediciones/"
ruta_especifica = "2024-12-26/"
nombre_archivo = "17-04-56_wf19_45_pmos35_K19_200x200_LCR_NBTI_PreStress.csv"
ruta_archivo = ruta_base + ruta_especifica + nombre_archivo

df = pd.read_csv( ruta_archivo )
#df['f_str']=df['f'].astype(str)
print(df)
print(df.dtypes)
#frec='1000.'
#df_aux=df[df['f_str'].str.contains('1000.0')]
#df_aux.to_csv(ruta_base + ruta_especifica + 'salida_prueba.csv')

ax=None
frec=[105,1000,300000,500000]
for i in frec:
    df_aux=df[df['f']==i]
    frec_str=str(int(i))
    #print('df_aux:\n', df_aux)
    ax=df_aux.plot(x='Vg', y='Cp', label='f (Hz): '+ frec_str, marker='o', linestyle='dashed',ax=ax)
plt.legend(loc='best')
plt.show()
