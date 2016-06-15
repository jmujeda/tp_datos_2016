# -*- coding: utf-8 -*- 
#https://www.kaggle.com/kobakhit/digit-recognizer/digit-recognizer-in-python-using-cnn
#1er submit de prueba, vainilla
#2do submit usando 200 n_stimators subió el score en 0.00086, quedando en 0.96629
#3er submit usando 200 n_stimatos y train blanco y negro, separando menores de  20 y mayores de 20. Esto dio 0.95400, menor a 0.96629 del submit2 
#4to submit usando trainYtest.csv, emperó dando 0.96543
#5to submit usando trainYtest.csv y 800 estimators, generando submission_tYt2.csv
#6to submit usando el set de entrenamiento ampliado 4 veces usando ampliador.py mejoró creo 0.5%
#submit sobre set BN ampliado = 0.97029
#
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import timeit

ENTRENAMIENTO = "_train_bn.csv"
TEST = "_test_bn.csv"
RESULTADO = "submission.csv" #archivo de salida con las predicciones
global VERBOSE
VERBOSE = 0

def rf(ENTRENAMIENTO, TEST, RESULTADO):
	print "Aplicando RF " + ENTRENAMIENTO + " -> " + TEST 
	a = timeit.default_timer()

	# create the training & test sets, skipping the header row with [1:]
	dataset = pd.read_csv(ENTRENAMIENTO)
	target = dataset[[0]].values.ravel()
	train = dataset.iloc[:,1:].values
	test = pd.read_csv(TEST).values

	# create and train the random forest
	# multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)

	# n_estimators < 200 empeora, por arriba de 200 deja de mejorar. Cuanto más alto, peor performance
	#para el set ampliado (8R), usa 6gb de ram. 4jobs tarda 3m20s 

	rf = RandomForestClassifier(n_estimators=250, n_jobs=4,verbose=VERBOSE)
	rf.fit(train, target)
	pred = rf.predict(test)

	np.savetxt(RESULTADO, np.c_[range(1,len(test)+1),pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')

	b = timeit.default_timer()
	secs = b - a
	m, s = divmod(secs,60)
	m = int(m)
	s = int(s)
	print "Fin (" + str( m) + ":" + str(s ) + ")"

if __name__ == '__main__':
	rf(ENTRENAMIENTO,TEST,RESULTADO)	