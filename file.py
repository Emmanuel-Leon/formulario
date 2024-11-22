import pandas as pd 

path = ('DEUDORES Y BAJAS SEM43.xlsx')

df = pd.read_excel(path, sheet_name='BAJAS SEM43')

profesores = df['Nombre del profesor']

name = "JESUS EMMANUEL DOMINGUEZ"

columna=len(profesores)
for i in range(columna):
    if(name==profesores[i]):
        alumno = df.iloc[i, 2]
        tel = df.iloc[i, 8]
        mat = df.iloc[i,0]
        grupo = df.iloc[i,5]
        hor = df.iloc[i,6]

        print (tel, '\n', alumno, '\n', grupo, '\n', hor, '\n', tel)

df = pd.read_excel(path, sheet_name ='DEUDORES DEM43')

profesores = df['Nombre del profesor']
name = 'JESUS EMMANUEL DOMINGUEZ'

for i in range(columna):
	if(name==profesores[i]):
		alumno = df.iloc[i,2]
		tel = df.iloc[i,8]
		mat = df.iloc[i,0]
		grupo = df.iloc[i,5]
		hor = df.iloc[i,6]

		print (mat,'\n', alumno, '\n', grupo,'\n', hor, '\n',tel )

