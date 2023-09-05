# script para graficar un archivo de mediciones .med del instrumento K2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Configuración del script:

nombre_archivo = 'archivo_med_k2.med2.txt'
canales_activos = [1, 2, 3, 4]
paso_temporal = 30  # seg

# Inicio del script

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
matriz = []
tiempo = []
while linea_actual != '':
    dato_s = []
    dato_s.append(linea_actual[-12:-1])
    dato_s.append(linea_actual[-24:-13])
    dato_s.append(linea_actual[-36:-25])
    dato_s.append(linea_actual[-48:-37])
    # print(dato_s[0])
    # print(dato_s[1])
    # print(dato_s[2])
    # print(dato_s[3])    
    # dato_s=['','','','']
    # dato_s[0]=linea_actual[-12:-1]
    # dato_s[1]=linea_actual[-24:-13]
    # dato_s[2]=linea_actual[-36:-25]
    # dato_s[3]=linea_actual[-48:-37]
    dato_f = []
    for i in range(4):
        dato_f.append(float(dato_s[i]))
    matriz.append(dato_f)
    tiempo.append(linea_num*paso_temporal)
    linea_actual = f_archivo.readline()
    linea_num += 1

print(f'Dimension de la matriz: {len(matriz)}')
print(f'Dimension del vector tiempo: {len(tiempo)}')

# cerrar archivo
f_archivo.close()

# Grafico:
labels_datos = ['canal#1','canal#2', 'canal#3', 'canal#4']
df = pd.DataFrame(matriz, index=tiempo, columns=labels_datos)
#df=df.cumsum() # Return cumulative sum over a DataFrame or Series axis

# Otro ejemplo de DataFrame:
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

# df3 = pd.DataFrame(
#     index=tiempo,
#     {
#         labels_datos[0]: matriz[:][0],
#         labels_datos[1]: matriz[:][1],
#         labels_datos[2]: matriz[:][2],
#         labels_datos[3]: matriz[:][3],
#     }
# )

df.plot()
plt.show();
#plt.legend(loc='best');
