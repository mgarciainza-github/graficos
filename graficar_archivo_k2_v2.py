# script para graficar un archivo de mediciones .med del instrumento K2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time

# Configuración del script:
<<<<<<< HEAD
path = '/home/mariano/Docs-GoogleDrive/Escritorio/varios/2023 varios/Sensor Radiacion Satelite 2023/irrad-sr90-fading/'
#path = '/home/mariano/docs-google-drive/Escritorio/varios/2023 varios/Sensor Radiacion Satelite 2023/irrad-sr90-fading/'
=======


#path = '/home/mariano/Docs-GoogleDrive/Escritorio/varios/2023 varios/Sensor Radiacion Satelite 2023/irrad-sr90-fading/'
path = '/home/mariano/docs-google-drive/Escritorio/varios/2023 varios/Sensor Radiacion Satelite 2023/irrad-sr90-fading/'
>>>>>>> 59a35256d32a592aafb8a7eb605e5bb46f17da5c
nombre_archivo = 'Track Vt - 05-06-2023_CD4007_para_sate_irrad_fading.med.txt'
paso_temporal = 2 # paso temporal del archivo de datos en segundos
canales_activos = ['c1', 'c2'] #lista de canales activos
rango_t=[0,0] # rango de tiempo a graficar en seg ([0,0] grafica todo)
rango_y=[0,0] # rango del eje y a graficar ([0,0] grafica todo)
tit='Titulo grafico'

# abrir el archivo
f_in=open(path + nombre_archivo,'r')

# OBS: probar de reescribir usando 'with' ... por ejemplo:
# with open("geeksforgeeks.txt","r") as gfg_file:
#    file_content = gfg_file.read()
#    print(file_content)


# saltear el encabezado y buscar el inicio de los datos:
linea_actual=f_in.readline()
while linea_actual != '':
    if linea_actual[0:5]=='time\t': 
        break
    else:
        linea_actual=f_in.readline()

print('generando archivo archivo_temp2.csv ...')
# reemplazar tab por coma en archivo temp
f_out=open(path + "archivo_temp2.csv",'w')
linea_nueva=''
while linea_actual != '':
    linea_nueva=linea_actual.replace('\t',',')
    linea_nueva=linea_nueva.replace('/','-')
    linea_nueva=linea_nueva.replace('  ',' ')
    linea_nueva=linea_nueva.replace('.000000','')
    f_out.write(linea_nueva)
    linea_actual=f_in.readline()

# cerrar archivos
f_in.close()
f_out.close()

print('generando df..')
# Dataframe
df = pd.read_csv(path + 'archivo_temp2.csv')
os.remove(path + 'archivo_temp2.csv')
#df.colums= ['t','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11']
df.rename(columns={'time':'fecha', 'Y[0]':'c1','Y[1]':'c2','Y[2]':'c3','Y[3]':'c4', \
                   'Y[4]':'c5','Y[5]':'c6','Y[6]':'c7','Y[7]':'c8','Y[8]':'c9', \
                   'Y[9]':'c10','Y[10]':'c11','Y[11]':'c12'}, inplace=True)

# Hay que generar una columna temporal a partir de la fecha y hora:
df['hora']=df['fecha'].str[11:]
#print(df['fecha'].str[11:])
df['seg'] = pd.to_timedelta(df['hora']).astype('timedelta64[s]').astype(int)

# Cuando cambia el día hay un salto en la commna 'seg'. Hay que corregir esa discontinuidad:
df['t']= 0
i_col_seg= len(df.columns)-2
i_col_t =  len(df.columns)-1
segundos_dia = 24*3600
print('generando col t (for)..')
for fila in range(len(df)-1):
    delta_seg = df.iloc[fila+1,i_col_seg] - df.iloc[fila,i_col_seg]
    if delta_seg < 0:
        delta_seg=delta_seg + segundos_dia
    df.iat[fila+1,i_col_t] = df.iloc[fila,i_col_t] + delta_seg

#df['t'] = df['seg']-df['seg'][0]
#df.to_csv(path + 'archivo_temp3.csv', index=False)

print('plot..')
# grafico:
#df.plot(y='t')
#df.plot( y = canales_activos, title =tit , marker='*', linestyle='dashed')
df.plot(x = 't', y = canales_activos, title =tit , marker='*', linestyle='dashed')
if rango_y != [0,0]: plt.ylim(rango_y)
if rango_t != [0,0]: plt.xlim(rango_t)
plt.show()
#plt.show(block=False)
<<<<<<< HEAD
=======

>>>>>>> 59a35256d32a592aafb8a7eb605e5bb46f17da5c
#input()



# REVISAR ANTES DE BORRAR:
# # Busqueda del inicio de los datos dentro del archivo .med
# linea_actual = f_archivo.readline()
# while linea_actual != '':
#     if linea_actual[0:5] == 'time\t':
#         break
#     else:
#         linea_actual = f_archivo.readline()

# linea_actual = f_archivo.readline()
# linea_num = 1

# # hay que sacar los datos de líneas como la siguiente, dónde VGS son las últmas 4 columnas:
# # 31/12/1903  21:00:00.000000	2.514548E+1	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	3.196639E+1	2.721465E+1	0.000000E+0	0.000000E+0
# #
# matriz = []
# tiempo = []
# while linea_actual != '':
#     dato_s = []
#     dato_s.append(linea_actual[-12:-1])
#     dato_s.append(linea_actual[-24:-13])
#     dato_s.append(linea_actual[-36:-25])
#     dato_s.append(linea_actual[-48:-37])
#     # print(dato_s[0])
#     # print(dato_s[1])
#     # print(dato_s[2])
#     # print(dato_s[3])    
#     # dato_s=['','','','']
#     # dato_s[0]=linea_actual[-12:-1]
#     # dato_s[1]=linea_actual[-24:-13]
#     # dato_s[2]=linea_actual[-36:-25]
#     # dato_s[3]=linea_actual[-48:-37]
#     dato_f = []
#     for i in range(4):
#         dato_f.append(float(dato_s[i]))
#     matriz.append(dato_f)
#     tiempo.append(linea_num*paso_temporal)
#     linea_actual = f_archivo.readline()
#     linea_num += 1

# print(f'Dimension de la matriz: {len(matriz)}')
# print(f'Dimension del vector tiempo: {len(tiempo)}')

# # cerrar archivo
# f_archivo.close()

# # Grafico:
# labels_datos = ['canal#1','canal#2', 'canal#3', 'canal#4']
# df = pd.DataFrame(matriz, index=tiempo, columns=labels_datos)
# #df=df.cumsum() # Return cumulative sum over a DataFrame or Series axis

# # Otro ejemplo de DataFrame:
# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )

# # df3 = pd.DataFrame(
# #     index=tiempo,
# #     {
# #         labels_datos[0]: matriz[:][0],
# #         labels_datos[1]: matriz[:][1],
# #         labels_datos[2]: matriz[:][2],
# #         labels_datos[3]: matriz[:][3],
# #     }
# # )

# df.plot()
# plt.show();
# #plt.legend(loc='best');
