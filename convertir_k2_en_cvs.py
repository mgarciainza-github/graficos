# idea para decimar sería cargar todo el datframe y luego procesarlo:
# 1) borrar primeras lineas del archivo hasta dejar encabezado
# 2) reemplazar '\t' por ',' para tener un csv y guardar archivo
# 3) crear el dat frame usando: df = pd.read_csv(download_url)
# 4) df.plot(x="Time", y=["Y[1]", "Y[3]"])
# 5) luego se puede usar iloc o loc para seleccionar filas..

archivo_de_entrada="/home/mariano/git-proyectos/marianogh03_graficos/a.txt"
archivo_de_salida ="/home/mariano/git-proyectos/marianogh03_graficos/a.csv"

# abrir el archivo
f_in=open(archivo_de_entrada,'r')
f_out=open(archivo_de_salida,'w')

# saltear el encabezado y buscar el inicio de los datos:
linea_actual=f_in.readline()
print(type(linea_actual))
while linea_actual != '':
    if linea_actual[0:5]=='time\t': 
        break
    else:
        linea_actual=f_in.readline()
print(linea_actual)
linea_nueva=''
# reemplazar tab por coma:
while linea_actual != '':
    # i=0
    # while linea_actual[i]!='\n':
    #     if linea_actual[i]=='\t':
    #         linea_nueva.append(',')
    #     else:
    #         linea_nueva.append(linea_actual[i])
    #     i+=1
    linea_nueva=linea_actual.replace('\t',',')
    print(f'esta es una linea nueva: {linea_nueva}')
    f_out.write(linea_nueva)
    linea_actual=f_in.readline()

# cerrar archivos
f_in.close()
f_out.close()