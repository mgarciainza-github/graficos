# Ejemplo para manipular filas y columnas de un df

import pandas as pd
import numpy as np
import os

os.system('clear')


# 0: creo un df:
dicc={'c1':[],'c2':[],'c3':[]}
print(type(dicc))
df = pd.DataFrame(dicc)
print(type(df))

# otra forma de crear un df:
df2 = pd.DataFrame([], index = ['indice_1','indice_2'], columns = ['c1','c2','c3'])

# 1: agrego filas a df
df.loc[0] = ['texto00',0,36 ]
print('1.1:\n',df,end='\n\n')
df.loc[len(df)]= ['texto01',1,22]
df.loc[len(df)]= ['texto02',2,6]
df.loc[len(df)]= ['texto03',3,4]
df.loc[len(df)]= ['otro1',4,3]
df.loc[len(df)]= ['otro2',5,2.5]
df.loc[len(df)]= ['otro3',6,9]
df.loc[len(df)]= ['otro1',8,11]

print('1:\n',df,end='\n\n')

# 2: quito/borro una fila
df.drop(1,inplace=True)
df.reset_index(inplace=True)
print('2:\n', df,end='\n\n')

#3: quito/borro una columna
df.drop('index',axis='columns',inplace=True)
print('3:\n',df,end='\n\n')

#4: ordeno
df.sort_values(by='c1',ascending=True, inplace=True)
print('4:\n',df,end='\n\n')

df.loc[len(df),'c1']=['abc']
df.loc[len(df),'c2']=[100]
df.loc[len(df)-1,'c1']=['abc']
df.loc[len(df),'c3']=[1000]
df.loc[len(df)-1,'c3']=[3000]
df.loc[len(df)-1,'c1']=['abc']

print('4:\n',df,end='\n\n')

#5: selecciono rangos
df_sel1 = df.loc[ (df['c3']>3) & (df['c3']<100) ]
#print('df_sel1 = df.loc[ (df[\'c3\']>3) & (df[\'c3\']<100) ]')
print('5.1:\n',df_sel1,end='\n\n')

df_sel2 = df.loc[ (df['c2']>5) & (df['c2']<4) ]
#print('df_sel1 = df.loc[ (df[\'c2\']>5) & (df[\'c2\']<4) ]')
print('5.2:\n',df_sel2,end='\n\n')

#6: selecciono por contenido
lista=['otro1','texto03','texto']
df_sel3 = df.loc[ df['c1'].isin(lista) ]
#print('df_sel3 = df.loc[ (df[\'c1\'].isin(lista))]' )
print('6.1:\n',df_sel3,end='\n\n')

df_sel4 = df[df['c1'].str.contains('xt') ]
print('6.2:\n',df_sel4,end='\n\n')

df_sel5 = df[df['c1'].str.match('xt') ]
print('6.3:\n',df_sel5,end='\n\n')

