# script para graficar un dit a patir de archivos de csv obtenido de mediciones CV multilista_frec en Nanolab 

# Pendientes:
# 1. Automatizar la manipulacion de archivos: indicar la fecha y que haga todo solo...
# 2. Guardar los resultados: df con dits e imágenes de los gráficos

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.system('clear')

# Configuración del script:
ruta_base = "/home/mariano/Docs-GoogleDrive/Nanolab/mediciones/"
ruta_especifica = "2024-12-26/"
nombre_archivo_pre = "17-04-56_wf19_45_pmos35_K19_200x200_LCR_NBTI_PreStress.csv"
nombre_archivo_pos = "17-04-56_wf19_45_pmos35_K19_200x200_LCR_NBTI_PostStress.csv"
#ruta_archivo = ruta_base + ruta_especifica + nombre_archivo

df_pre = pd.read_csv( ruta_base + ruta_especifica + nombre_archivo_pre )
df_pos = pd.read_csv( ruta_base + ruta_especifica + nombre_archivo_pos )
#df['f_str']=df['f'].astype(str)
#print(df)
#print(df.dtypes)
#lista_frec='1000.'
#df_aux=df[df['f_str'].str.contains('1000.0')]
#df_aux.to_csv(ruta_base + ruta_especifica + 'salida_prueba.csv')

# Graficos CV
'''
ax=None
lista_frec=[105,1000,300000,500000]
for i in lista_frec:
    df_aux=df_pre[df_pre['f']==i]
    lista_frec_str=str(int(i))
    #print('df_aux:\n', df_aux)
    ax=df_aux.plot(x='Vg', y='Cp', label='f (Hz): '+ lista_frec_str, marker='o', linestyle='dashed',ax=ax)
plt.legend(loc='best')
plt.title('CVs Pre')
plt.show(block=False)
ax=None
for i in lista_frec:
    df_aux=df_pos[df_pos['f']==i]
    lista_frec_str=str(int(i))
    #print('df_aux:\n', df_aux)
    ax=df_aux.plot(x='Vg', y='Cp', label='f (Hz): '+ lista_frec_str, marker='o', linestyle='dashed',ax=ax)
plt.legend(loc='best')
plt.title('CVs Pos')
#plt.show()
plt.show(block=False)
'''

# Dit
## tomo el valor de cox a f=1k en acumulación Vg=1
# df_cox = df_pre[ (df_pre['f']==1000) & (df_pre['Vg']==1) ]
# df_cox.reset_index(inplace=True)
# cox=df_cox.loc[0,'Cp']
q = 1.60217663e-19 # Coul
A = 200*200e-8 # cm-2
ax=None
lista_frec=[105,1000,300000,500000]
for f in lista_frec:
    df_aux=pd.DataFrame()
    df_aux_pre = df_pre[df_pre['f']==f]
    df_aux_pos = df_pos[df_pos['f']==f]
    filtro=5
    if f < 1000: # simple moving average / filtro pasa bajo para reducir el ruido 
    	df_aux_pre['Cp'] = df_aux_pre['Cp'].rolling(window=filtro).mean()
    	df_aux_pos['Cp'] = df_aux_pos['Cp'].rolling(window=filtro).mean()
    print(df_aux_pre)
    df_aux['delta_cp'] = (df_aux_pos['Cp']-df_aux_pre['Cp'])
    df_aux['Vg'] = df_pos[df_pos['f']==f].loc[:,'Vg']
    df_aux['Dit'] = df_aux['delta_cp']/(q*A)
    frec_str=str(f/1000)
    #print('df_aux:\n', df_aux)
    etiqueta = 'f(kHz): ' + frec_str
    if f < 1000:
	    etiqueta = etiqueta + 'c/filtro: ('+ str(filtro) + ')' 
    ax=df_aux.plot(x='Vg', y='Dit', label=etiqueta, marker='o', linestyle='dashed',ax=ax)
    del df_aux
plt.legend(loc='best')
plt.title('Dit')
#plt.show(block=False)
plt.show()

#df_aux.to_csv(ruta_base + ruta_especifica + 'salida_prueba.csv')
