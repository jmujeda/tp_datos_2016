# -*- coding: utf-8 -*- 
#La idea de este archivo es multiplicar los registros del set de entrenamiento para ver como varia.
#Para no meter las repeticiones de los registros todas juntas las voy a meter en un buffer e insertar las lineas una por una una vez que se llene el mismo

#OJO: con 10 copias se hizo muy pesado el RF y me colgó la máquina. 
#Con 4 copias anduvo bien y mejoró el RF un 0.5%
import csv

REPETICIONES = 4 #Define cuantas copias se van a hacer
TAM_BUFFER = 100
_buffer = [None] * (TAM_BUFFER + 1)
NUEVO_SET = "train_con_" + str(REPETICIONES) + "_reps.csv"
header = True

for x in range(0,REPETICIONES):
	f = open("train.csv")
	destino = open(NUEVO_SET,"a+")
	wr = csv.writer(destino, quoting=csv.QUOTE_NONE)

	i = 0
	buffer_lleno = False

	for linea in f:
		if header:
			header = False
			continue
		_buffer[i] = linea

		if i == TAM_BUFFER:
			i = 0
			buffer_lleno = True

		destino.write(linea)
		if buffer_lleno == True:
			destino.write(_buffer[i])

		i += 1

	f.close()
	#Al terminar vacio el buffer
	for j in _buffer:
		destino.write(j)

	destino.close()
	header = True