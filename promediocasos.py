import matplotlib.pyplot as plt
import sqlite3
conn = sqlite3.connect('casoscovidmx.sqlite')
cur = conn.cursor()

cur.execute('''SELECT Estado FROM COVIDMX''')
estados=list()
for row in cur:
    for i in row:
        estados.append(i)
cur.execute(''' SELECT Promedio_casos_diarios FROM COVIDMX''')
casos=list()
for row in cur:
    for i in row:
        casos.append(i)


xAxis=estados
yAxis=casos
plt.figure(figsize=(13,6))
plt.barh(xAxis,yAxis, color='red', edgecolor='black')

i=1.0
j=1000
for i in range(len(estados)):
    plt.annotate(casos[i], (-0.1+i,casos[i]+j))
plt.title('Casos confirmados de Covid en México por Estado',fontsize=16)
plt.xlabel('Casos confirmados diarios en promedio',fontsize=14)
plt.ylabel('Estados',fontsize=14)
plt.show()
