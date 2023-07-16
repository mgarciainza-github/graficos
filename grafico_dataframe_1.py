import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# grafico simple: grafica dataframes de pandas
# https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html?m=1

# genero algunos datos a graficar en una lista:
datos=[['tiempo','med_1', 'med_2','med_3'], [10,0.1,0.01,.5],[20,.23,.023,.4],[30,.34,.034,.6],[40,.22,.022,0.1],[50,0.1,0.01,.5],[60,.23,.023,.4],[70,.34,.034,.6],[80,.22,.022,0.1]]
print(f'datos como una lista: {datos}')

# paso la lista a dataframe:
df = pd.DataFrame(datos[1:], columns=datos[0])
print(f'datos como una df: \n {df}')

# grafico 
df.plot(x='tiempo', y=['med_1','med_3','med_2'], title='grafico df', marker='x')
plt.show(block=False)
##df.plot(kind='scatter',x='tiempo', y=['med_3'])
##df.plot.scatter(x='tiempo', y=['med_3'])
#plt.show()

# otro grafico con algunas filas seleccionadas con iloc
#df2=df.iloc[0:4,] 
#df2=df.iloc[0:4,:2] 
df2=df.iloc[2:7,:]
tit2='df2=df.iloc[2:7,:]'
print(f'datos df2: \n{df2}')
df2.plot(x='tiempo', y=['med_1','med_3','med_2'], title=tit2, linewidth=3, marker ='*'); 
plt.show(block=False)

# otro grafico con algunas filas seleccionadas con loc
df3=df.loc[(df.tiempo>20) & (df.tiempo<70)] 
tit3='df3=df.loc[(df.tiempo>10) & (df.tiempo<70)]'
print(f'datos df3: \n{df3}')
df3.plot(x='tiempo', y=['med_1','med_3','med_2'], title=tit3, linestyle='dashed', marker='o'); 
plt.show(block=False)

df3.plot(x='tiempo', y=['med_3'], title=tit3, linestyle='dashed', marker='o'); 
plt.show(block=False)

# espera enter para cerrar las figuras
input()
