# script para graficar un archivo de cvs gnerico
# ******* EN DESARROLLO 4-sep-23 *******

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Configuración del script:

#ruta_base = '/home/mariano/Docs-GoogleDrive/Descargas/23_Allegro-UTN/shottky/'
#ruta_especifica = 'med_directa_dist_areas_y_dist_temp/6x6_csv/'
#nombre_archivo = 'site2.1_tile4_device23_-5to5_0C.csv'
#ruta_archivo = ruta_base + ruta_especifica + nombre_archivo

ruta_base = "/home/mariano/github/marianogh03_graficos/"
ruta_especifica = ""
nombre_archivo = "a.csv"
ruta_archivo = ruta_base + ruta_especifica + nombre_archivo

df = pd.read_csv( ruta_archivo )
#print(df)

df.rename(columns = {'time':'Date'}, inplace = True)
df.rename(columns = {'Y[0]':'Y00', 'Y[1]':'Y01', 'Y[2]':'Y02','Y[3]':'Y03','Y[4]':'Y04' }, inplace = True)

# agregar columna de tiempo en segundos time(s) siendo que la primera columna es un string con la fecha y hora: "31/12/1903  21:00:00.000000"
date_str = df.iat[0,0]
t_zero = 10*3600*int(date_str[12]) + 3600*int(date_str[13]) + 10*60*int(date_str[15]) + 60*int(date_str[16]) + 10*int(date_str[18]) + int(date_str[19]) + 0.1*int(date_str[21])
date_str=df.iat[11,0]

largo = df.shape[0]
t_list=[]
for x in range(largo):
    date_str=df.iat[x,0]
    #print(date_str)
    t_value = 10*3600*int(date_str[12]) + 3600*int(date_str[13]) + 10*60*int(date_str[15]) + 60*int(date_str[16]) + 10*int(date_str[18]) + int(date_str[19]) + 0.1*int(date_str[21]) 
    t_list.append(str(t_value - t_zero))

#print('---')
#print(t_list)

#print('---')
df.insert(1, "Time(s)", t_list, True)
print(df)


#graficos:

#df.plot(x='v_a', y='i_a', logy=True, title=nombre_archivo, marker='o', linestyle='dashed', color='red')
#df.plot(x='v_a', y='i_a', title=nombre_archivo, marker='x', linestyle='dashed', color='blue')


df.plot(x='Time(s)', y='Y00', logy=True, title=nombre_archivo, marker='o', linestyle='dashed', color='red')
df.plot(x='Time(s)', y='Y[8]', logy=True, title=nombre_archivo, marker='o', linestyle='dashed', color='blue')
df.plot(x='Time(s)', y='Y[9]', logy=True, title=nombre_archivo, marker='o', linestyle='dashed', color='green')

plt.show(block=False)
plt.show()
