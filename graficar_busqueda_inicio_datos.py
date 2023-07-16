# script para graficar un archivo de mediciones del instrumento K2

nombre_archivo='archivo_med_k2.med.txt'

f_archivo=open(nombre_archivo,'r')

linea_actual=f_archivo.readline()

while linea_actual != '':
    if linea_actual[0:5]=='time\t':
        print('Encontré la línea!', end=' ')
        print(linea_actual)
        break
    else:
        print('No es la línea deseada, es:', end=' ')
        print(linea_actual)
        linea_actual=f_archivo.readline()

print('Fin del while.')
linea_actual=f_archivo.readline()
print('La primera línea de datos es:')
print(linea_actual)

# cerrar archivos
f_archivo.close()

