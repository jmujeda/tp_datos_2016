
import csv

#Este programa expande el archivo de entrenamiento con los resultados de las predicciones del archivo de test.

#Necesita el archivo de entrenaminto, el de test, y un submit del archivo de test, y devuelve un nuevo archivo de entrenamiento
#compuesto por el archivo de entrenamiento + el submit de test

#Notar que el archivo submission tiene solamente una línea para cada predicción, ej:
#1
#4
#9
#2
#3
#etc

#por lo que este archivo joinea esos resultados con cada línea de test.csv

TRAIN = "train.csv"
TEST = "test.csv"
SUBMISSION = "submission.csv"
NUEVO_TRAIN = "trainYtest.csv"

def run():
	f = open(TRAIN)
	fOutput = open(NUEVO_TRAIN,"a")
	wr = csv.writer(fOutput, quoting=csv.QUOTE_NONE)
	i = -1

	for linea in f:
		fOutput.write(linea)
	f.close()
	
	fSub = open(SUBMISSION)
	fTest = open(TEST)
	

	lineaTest = fTest.readline()
	lineaSub = fSub.readline()

	#Leo 2 veces para saltear el encabezado
	lineaTest = fTest.readline().rstrip('\n').rstrip('\r')
	lineaSub = fSub.readline().rstrip('\n').rstrip('\r')

	while (lineaTest):
		lT = lineaTest.split(',')		
		lS = lineaSub.split(',')

		res = lS[1:] + lT
		wr.writerow(res)
		
		lineaTest = fTest.readline().rstrip('\n').rstrip('\r')
		lineaSub = fSub.readline().rstrip('\n').rstrip('\r')
	
	fSub.close()
	fTest.close()
	fOutput.close()
	
run()