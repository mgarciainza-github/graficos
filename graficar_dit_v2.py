# script para graficar un dit a patir de archivos de csv obtenido de mediciones CV multifrec en Nanolab 

# Pendientes:
# 1. Automatizar la manipulacion de archivos: indicar la fecha y que haga todo solo...
# 2. Guardar los resultados: df con dits e imágenes de los gráficos

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from os import listdir
from os.path import isfile, join


os.system('clear')

# Configuración del script:
ruta_base = "/home/mariano/Docs-GoogleDrive/Nanolab/mediciones/"
fecha_medicion = "2024-12-26"
ruta_especifica = fecha_medicion + "/"
ruta = ruta_base + ruta_especifica
lista_archivos = [f for f in listdir(ruta) if isfile(join(ruta, f))]
nombre_archivo_pre =  [f for f in lista_archivos if (f.find('PreStress'))!=(-1)][0]
nombre_archivo_pos =  [f for f in lista_archivos if (f.find('PostStress'))!=(-1)][0]
#nombre_archivo_pre = "17-04-56_wf19_45_pmos35_K19_200x200_LCR_NBTI_PreStress.csv"
#nombre_archivo_pos = "17-04-56_wf19_45_pmos35_K19_200x200_LCR_NBTI_PostStress.csv"
#ruta_archivo = ruta_base + ruta_especifica + nombre_archivo
df_pre = pd.read_csv( ruta + nombre_archivo_pre )
df_pos = pd.read_csv( ruta + nombre_archivo_pos )
#print(df)
#print(df.dtypes)

# Graficos CV
ax=None
frec=[105,1000,300000,500000]
for i in frec:
    df_aux=df_pre[df_pre['f']==i]
    frec_str=str(int(i))
    #print('df_aux:\n', df_aux)
    ax=df_aux.plot(x='Vg', y='Cp', label='f (Hz): '+ frec_str, marker='o', linestyle='dashed',ax=ax)
plt.legend(loc='best')
plt.title('CVs Pre')
plt.show(block=False)
ax=None
for i in frec:
    df_aux=df_pos[df_pos['f']==i]
    frec_str=str(int(i))
    #print('df_aux:\n', df_aux)
    ax=df_aux.plot(x='Vg', y='Cp', label='f (Hz): '+ frec_str, marker='o', linestyle='dashed',ax=ax)
plt.legend(loc='best')
plt.title('CVs Pos')
#plt.show()
plt.show(block=False)

df_aux.to_csv(ruta + 'archivo_salida_prueba_00000.csv')

# Dit
## tomo el valor de cox a f=1k en acumulación Vg=1
# df_cox = df_pre[ (df_pre['f']==1000) & (df_pre['Vg']==1) ]
# df_cox.reset_index(inplace=True)
# cox=df_cox.loc[0,'Cp']
q = 1.60217663e-19 # Coul
A = 200*200e-8 # cm-2
ax=None
df_dit=pd.DataFrame()
frec=[105,1000,300000,500000]
for i in frec:
    df_aux=pd.DataFrame()
    df_aux_pre = df_pre[df_pre['f']==i]
    df_aux_pos = df_pos[df_pos['f']==i]
    if i < 1000: # simple moving average / filtro pasa bajo para reducir el ruido 
    	df_aux_pre.loc[:,'Cp'] = df_aux_pre.loc[:,'Cp'].rolling(window=5).mean()
    	df_aux_pos.loc[:,'Cp'] = df_aux_pos['Cp'].rolling(window=5).mean()
    #print(df_aux_pre)
    df_aux['delta_cp'] = (df_aux_pos['Cp']-df_aux_pre['Cp'])
    df_aux['Vg'] = df_pos[df_pos['f']==i].loc[:,'Vg']
    df_aux['Dit'] = df_aux['delta_cp']/(q*A)
    frec_str=str(int(i))
    #print('df_aux:\n', df_aux)
    ax=df_aux.plot(x='Vg', y='Dit', label='f (Hz): '+ frec_str, marker='o', linestyle='dashed',ax=ax)
    df_dit=pd.concat([df_dit,df_aux]) 	
    del df_aux
plt.legend(loc='best')
plt.title('Dit')
#plt.show(block=False)
plt.show()

df_dit.to_csv(ruta + 'archivo_salida_prueba_00001.csv')


