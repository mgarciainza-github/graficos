#Ejemplo para armar un df a partir de datos varios en dos columnas con 'tags'

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

os.system('clear')

# genero algunos datos
x = np.linspace(0,10,30)
y1 = 2*x + 0.7
y2 = 1.1*x**2
y3 = .77*np.exp(x*0.5)
tag1='lin'
tag2='cuad'
tag3='exp'
""" 
plt.plot(x,y1,marker='D')
plt.plot(x,y2,marker='o')
plt.plot(x,y3,marker='s')
plt.xlabel('Posición (m)')
plt.xlabel('Velocidad (m/s)')
plt.title('Velocidad durante la carrera')
plt.legend((tag1,tag2,tag3),frameon=False)
plt.show()

 """
 
# armo el dataframe:
df=pd.DataFrame({'x':[],'y':[],'tag':[]})
df.x=x
df.y=y1
df.tag[0:len(df)]=tag1
print('paso1:\n',df,end='\n\n')

df_aux=pd.DataFrame({'x':[],'y':[],'tag':[]})
df_aux.x=x
df_aux.y=y2
df_aux.tag[0:len(df)]=tag2
print('paso2:\n',df_aux,end='\n\n')

df=pd.concat([df,df_aux])
df.reset_index(inplace=True)
df.drop('index',axis='columns',inplace=True)
del df_aux

print('paso3:\n',df,end='\n\n')

df_aux=pd.DataFrame({'x':[],'y':[],'tag':[]})
df_aux.x=x
df_aux.y=y3
df_aux.loc[0:len(df),'tag']=tag3
print('paso3:\n',df_aux,end='\n\n')

df=pd.concat([df,df_aux])
df.reset_index(inplace=True)
df.drop('index',axis='columns',inplace=True)
del df_aux

df.to_csv('archivo_salida.csv')

df_aux = df[df['tag'].str.contains('ex') ]
print('6.2:\n',df_aux,end='\n\n')

df_aux.to_csv('archivo_salida_aux.csv')

plt.plot(df[df['tag'].str.contains(tag1)].x, df[df['tag'].str.contains(tag1)].y, marker='s')
plt.plot(df[df['tag'].str.contains(tag2)]['x'], df[df['tag'].str.contains(tag2)]['y'], marker='o')
plt.plot(df[df['tag'].str.contains(tag3)]['x'], df[df['tag'].str.contains(tag3)]['y'], marker='h')
plt.show()