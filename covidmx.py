#https://datos.covid-19.conacyt.mx/#DOView
# Para que esté actualizada debe descargar el csv más reciente de la siguiente página:https://datos.covid-19.conacyt.mx/#DOView
#deberá descargar la opción de casos confirmados que está dentro de 'Casos diarios por Estado + Nacional'
# y ponerlo en tu editor de texto
#guardar como 'casos covid' en formato CSV (delimitado por comas).
#ejecutar en command line covidmx.py dentro del lugar o folder donde esté este programa de Python.
import sqlite3
import csv

conn = sqlite3.connect('casoscovidmx.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS COVIDMX''')

cur.execute('''CREATE TABLE IF NOT EXISTS COVIDMX
    (id INTEGER UNIQUE, Estado TEXT, Población INTEGER, Máximo_diario INTEGER,
     Promedio_casos_diarios INTEGER, Casos_totales INTEGER)''')


fname=input('Enter file name:')
if len(fname)<1: fname='casos covid.csv'
casos=list()
print('Descargando información sobre los casos confirmados en México...')
print('Por favor espere...')
with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    id=None
    estado=None
    pob=None
    promcasos=None
    total=None
    maxdia=None
    count=0
    fecha=None
    for line in csv_reader:
        if 'nombre' in line:
            continue
        else:
            id=line[0]
            estado=line[2]
            pob=line[1]
            casostotales=line[3:]
            lista=list()
        for num in casostotales:
            count=count+1
            inum=int(num)
            lista.append(inum)
            maxdia=max(lista)
        if estado.lower() in estado: continue
        #print(id)
        #print(estado)
        #print(pob)
        #print(casostotales)
        total=sum(lista)
        #print(total)
        promcasos=round(total/count,2)
        #print(promcasos)
        cur.execute('''INSERT OR IGNORE INTO COVIDMX (id, Estado, Población, Máximo_diario, Promedio_casos_diarios, Casos_totales)
        VALUES ( ?, ?, ?, ?, ?, ? )''', (id, estado, pob, maxdia, promcasos, total))
        conn.commit()
print('Listo')
conn.commit()
conn.close()
