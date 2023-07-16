import matplotlib.pyplot as plt
import numpy as np

# grafico simple: permite agregar puntos a un gráfico "en tiempo real" para usar durante una medeción por ejemplo.

# Grafios separados
#fig, (ax1) = plt.subplots()
#fig, (ax2) = plt.subplots()

# Graficos en la misma ventana:
fig, (ax1,ax2) = plt.subplots(2,1)

# Para deshabilitar modo interactivo usar:
plt.show(block=False)

# genero los datos a graficar del primer punto:
datos=[['tiempo','med_1', 'med_2']]
tiempo=10
med_1=.1
med_2=.2
datos.append([tiempo,med_1,med_2])
#input()

# grafico el primer punto
ax1.plot(tiempo,med_1,'o',color='r')
ax1.set_xlabel('X en [s]', fontsize=14)
ax1.set_ylabel('Y en [V]', fontsize=14)
ax1.grid(True)
ax1.set_title('titulo med1 en tiempo real', fontsize=16)
fig.tight_layout()
#plt.pause(0.01)
ax2.plot(tiempo,med_2,'x', color='b')
ax2.set_xlabel('X en [s]', fontsize=14)
ax2.set_ylabel('Y en [V]', fontsize=14)
ax2.grid(True)
ax2.set_title('titulo med2 en tiempo real', fontsize=16)
fig.tight_layout()
#plt.pause(0.001)
#input()

# genero los datos a graficar de otro punto:
tiempo=20
med_3=.35
med_4=.45
datos.append([tiempo,med_3,med_4])
# agrego punto al gráfico:
ax1.plot(tiempo,med_3,'o',color='r')
#fig.tight_layout()
#plt.pause(0.01)
ax2.plot(tiempo,med_4,'x', color='b')
#fig.tight_layout()
plt.pause(0.001)
print('presionar enter para cerrar y salir')
print(datos)
input()