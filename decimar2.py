# script para decimar archivo de medicion de CD4007 con K2 

# otra idea para decimar sería cargar todo el datframe y luego procesarlo:
# 1) borrar primeras lineas del archivo hasta dejar encabezado
# 2) reemplazar '\t' por ',' para tener un csv y guardar archivo
# 3) crear el dat frame usando: df = pd.read_csv(download_url)
# 4) df.plot(x="Time", y=["Y[1]", "Y[3]"])
# 5) luego se puede usar iloc o loc para seleccionar filas..


archivo_de_salida="Track_Vt-05-06-2023_cd4007_para_sate_irrad_fading.med2_decimado.txt"
archivo_de_entrada="Track_Vt-05-06-2023_cd4007_para_sate_irrad_fading.med2.txt"

# factor de decimación (se muestrea cada 2 seg)
factor=5

# abrir el archivo
f_in=open(archivo_de_entrada,'r')
f_out=open(archivo_de_salida,'w')


i=0
linea_actual=f_in.readline()
while linea_actual != '':
#    print(i)
#    print(linea_actual)
    if (i%factor)==0:
        f_out.write(linea_actual)
#        print('Linea escrita en archivo:', end=' ')
#        print(i, end=' ')
#        print(linea_actual)
    i=i+1
    linea_actual=f_in.readline()

# cerrar archivos
f_in.close()
f_out.close()

