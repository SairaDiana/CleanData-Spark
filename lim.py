#Saira Diana Carranza Rodríguez
#Becario Big-Data en BEEVA
import pandas as pd
import numpy as np
import csv

#URL, donde se encuntra d dataset a trabajar
dataset= pd.read_csv('/home/administradorcito/Descargas/Xbox 7-day auctions.csv', header=0)

#Identificamos los valores nulos y la funcion any, nos ayuda a ver si cumplen con esa condicion
nulos=dataset.isnull().any().any()

#Agrupando los datos por tipos de datos las siguientes lineas identifican las variables categoricas, que en este caso corresponden a los nombres de usuario
tipos = dataset.columns.to_series().groupby(dataset.dtypes).groups
ctext = tipos[np.dtype('object')]
total=len(ctext)

#las siguientes lineas muestran las 6 variables numericas
columnas = dataset.columns 
cnum = list(set(columnas) - set(ctext))
numericas=len(cnum)

#En las variables numericas donde se encuantran valores nulos, se saca la media con la finalidad de equilibrar los datos y reemplazar los valores nulos por el calculo de la media
for c in cnum:
    mean = dataset[c].mean()
    dataset[c] = dataset[c].fillna(mean)

#Para las variables categoricas se busca la moda de los nombres de usuarios reemplaza los valores nulos por los nombres que mas se repiten
for c in ctext:
    mode = dataset[c].mode()[0]
    dataset[c] = dataset[c].fillna(mode)

#Por ultimo se identifica si despues de proceso anterio aun hay valores nulos
nonulos=dataset.isnull().any().any()

#Se guarda el dtaset como csv
dataset.to_csv("datanuevo.csv", index=False)
