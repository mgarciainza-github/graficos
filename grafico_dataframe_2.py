import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# grafico simple: grafica dataframes de pandas
# https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html?m=1

##############################################################################################
# configuración general de script
nombre_archivo = 'Track_Vt-05-06-2023_cd4007_para_sate_irrad_fading.med2_decimado.txt'
#canales: activos = 1, desactivados = 0
c1=1
c2=1
c3=1
c4=1
paso_temporal = 30  # seg
rango_temporal = [0, 0] # seg
rango_eje_y=[-1, 80]

##############################################################################################
# obtengo los datos del archivo de mediciones:
f_archivo = open(nombre_archivo, 'r')

# Busqueda del inicio de los datos dentro del archivo .med
linea_actual = f_archivo.readline()
while linea_actual != '':
    if linea_actual[0:5] == 'time\t':
        break
    else:
        linea_actual = f_archivo.readline()

linea_actual = f_archivo.readline()
linea_num = 1

# hay que sacar los datos de líneas como la siguiente, dónde VGS son las últmas 4 columnas:
# 31/12/1903  21:00:00.000000	2.514548E+1	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	0.000000E+0	3.196639E+1	2.721465E+1	0.000000E+0	0.000000E+0
#
datos = []
while linea_actual != '':
    dato_s = []
    dato_s.append(linea_actual[-12:-1])
    dato_s.append(linea_actual[-24:-13])
    dato_s.append(linea_actual[-36:-25])
    dato_s.append(linea_actual[-48:-37])
    tiempo = linea_num*paso_temporal
    dato_f = []
    dato_f.append(tiempo)
    for i in range(4):
        dato_f.append(float(dato_s[i]))
    datos.append(dato_f)
    linea_actual = f_archivo.readline()
    linea_num += 1
# cerrar archivo
f_archivo.close()

#print(f'Longitud del vector tiempo: {len(tiempo)}')
print(f'datos[0]: {datos[0]}')
print(f'datos[1]: {datos[1]}')

##############################################################################################

# armo el data frame:
columnas_datos=['tiempo','c1','c2','c3','c4']
df = pd.DataFrame(datos, columns=columnas_datos)
#print(f'datos como una df: \n {df}')
print('df.head()')
# df.head()
# df.head(-3)

# # grafico 
tit='Medicion realizada con K2'
#canales_activos = [c1*columnas_datos[1], c2*columnas_datos[2], c3*columnas_datos[3], c4*columnas_datos[4]]
canales_activos = []
if c1==1: canales_activos.append(c1*columnas_datos[1])
if c2==1: canales_activos.append(c2*columnas_datos[2])
if c3==1: canales_activos.append(c3*columnas_datos[3])
if c4==1: canales_activos.append(c4*columnas_datos[4])

print('canales_activos:')
print(canales_activos)
df.plot(x = 'tiempo', y = canales_activos, title =tit , marker='*', linestyle='dashed')
plt.ylim(rango_eje_y)
plt.show(block=False)

# # otro grafico con algunas filas seleccionadas con loc
# # df3=df.loc[(df.tiempo>20) & (df.tiempo<70)] 
# # tit3='df3=df.loc[(df.tiempo>10) & (df.tiempo<70)]'
# # print(f'datos df3: \n{df3}')
# # df3.plot(x='tiempo', y=['med_1','med_3','med_2'], title=tit3, linestyle='dashed', marker='o'); 
# # plt.show(block=False)

# # df3.plot(x='tiempo', y=['med_3'], title=tit3, linestyle='dashed', marker='o'); 
# # plt.show(block=False)

# # espera enter para cerrar las figuras
input()
