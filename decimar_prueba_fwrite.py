# script para decimar archivo de medicion de CD4007 con K2 

archivo_de_salida="Track_Vt-05-06-2023_cd4007_para_sate_irrad_fading.med3_fwrite.txt"

# factor de decimación (se muestrea cada 2 seg)
factor=1

# abrir el archivo
f_out=open(archivo_de_salida,'w')

linea_actual='hola1\n'
f_out.write(linea_actual)
linea_actual='hola2\n'
f_out.write(linea_actual)

# cerrar archivos
f_out.close()

