import pandas as pd


list1 = ['Matricula'    ,   'Nombre del alumno    ','     Comentario       ','Grupo  ','  Horario   ',' Telefono    ']
list2 = ['GD71191246','GOMEZ RODRIGUEZ DAVID','','COM1622','16:00-20:00','2282554566']
list3 = ['MM71191029', 'MARTINEZ LOPEZ MIGUEL ANGEL ','','COM1636','08:00-12:00',2282923078]
list4 = ['','','','','','']
list5 = ['','','','','','']
list6 = ['', '','','','','']

data = (list1,list2,list3,list4,list5,list6)

Df = pd.DataFrame(data)
Df.to_excel('DEUSEM35.xlsx')
