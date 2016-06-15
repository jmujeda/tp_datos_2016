# -*- coding: utf-8 -*- 
#La idea de este archivo es multiplicar los registros del set de entrenamiento para ver como varia.
#Para no meter las repeticiones de los registros todas juntas las voy a meter en un buffer e insertar las lineas una por una una vez que se llene el mismo

#OJO: con 10 copias se hizo muy pesado el RF y me colgó la máquina. 
#Con 4 copias anduvo bien y mejoró el RF un 0.5% 

#v2: no me cerraba el tamaño del archivo (era más pesado de lo esperado). Estaba guardando 2 veces las líneas, una mientras las leía y otra con el buffer
#Entonces,  cuando arriba puse 10 copias en realidad eran 20, y cuando puse 4 eran 8. Ya está corregido
import csv
import timeit

global REPETICIONES
REPETICIONES = 8 #Define cuantas copias se van a hacer
global TAM_BUFFER
TAM_BUFFER = 100
global _buffer
_buffer = [None] * (TAM_BUFFER + 1)
global NUEVO_SET
NUEVO_SET = "train_con_" + str(REPETICIONES) + "_reps2.csv"


global INPUT
INPUT = "train.csv"

def ampliar_set(f_input, f_output):
	
	print "Ampliando " + f_input 
	a = timeit.default_timer()

	header = True
	destino = open(f_output,"w")
	primera_pasada = True
	
	for x in range(0,REPETICIONES/2): #fix version 2.0
		f = open(f_input)

		wr = csv.writer(destino, quoting=csv.QUOTE_NONE)

		i = 0	
		buffer_lleno = False

		for linea in f:
			if header:
				header = False
				if primera_pasada:
					primera_pasada = False
					destino.write(linea)
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

		header = True

	destino.close()
	
	b = timeit.default_timer()
	secs = b - a
	m, s = divmod(secs,60)
	m = int(m)
	s = int(s)
	print "Fin (" + str( m) + ":" + str(s ) + ")"


if __name__ == '__main__':
	ampliar_set(INPUT, NUEVO_SET)