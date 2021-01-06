Para obtener la información actualizada se debe descargar en formato csv de la siguiente página:
https://datos.covid-19.conacyt.mx/#DOView
Deberá descargar la opción de casos confirmados que está dentro de 'Casos diarios por Estado + Nacional'
Guardar el archivo descargado como 'casos covid' en formato 'CSV (delimitado por comas)''.
Ejecutar en command line o Símbolo del sistema covidmx.py dentro del lugar o folder donde esté el programa de Python.
Cuando pide el nombre del archivo simplemente presione 'Enter'.
Generará una SQL con la información descargada del csv. EL nombre del SQl es 'casoscovidmx'.
Tendrá el Estado, su población e información sobre los casos confirmados de covid por cada Estado del país.
Para poder observar las distintas gráficas que se pueden generar están los siguientes programas:
graficamaximos.py
graficapais.py
promediocasos.py
Las gráficas son una muestra de la información recopilada al 27 de diciembre de 2020, al igual que el documento 'casos covid.csv'
Se pueden generar otras gráficas con la información disponible, para lo cual cualquier persona lo puede modificar.
