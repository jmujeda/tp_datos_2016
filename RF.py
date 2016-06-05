# -*- coding: utf-8 -*- 
#https://www.kaggle.com/kobakhit/digit-recognizer/digit-recognizer-in-python-using-cnn
#1er submit de prueba, vainilla
#2do submit usando 200 n_stimators subió el score en 0.00086, quedando en 0.96629
#3er submit usando 200 n_stimatos y train blanco y negro, separando menores de  20 y mayores de 20. Esto dio 0.95400, menor a 0.96629 del submit2 
#4to submit usando trainYtest.csv, emperó dando 0.96543
#5to submit usando trainYtest.csv y 800 estimators, generando submission_tYt2.csv
#6to submit usando el set de entrenamiento ampliado 4 veces usando ampliador.py mejoró creo 0.5%

from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

ENTRENAMIENTO = "train_con_4_reps.csv"
TEST = "test.csv"
RESULTADO = "submission.csv" #archivo de salida con las predicciones

# create the training & test sets, skipping the header row with [1:]
dataset = pd.read_csv(ENTRENAMIENTO)
target = dataset[[0]].values.ravel()
train = dataset.iloc[:,1:].values
test = pd.read_csv(TEST).values

# create and train the random forest
# multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)

# Ojo, n_jobs=2 usa más cpus, pero creo que a su vez aumenta el consumo de ram
# n_estimators < 200 empeora, por arriba de 200 deja de mejorar. Cuanto más alto, peor performance

rf = RandomForestClassifier(n_estimators=200, n_jobs=1,verbose=10)
rf.fit(train, target)
pred = rf.predict(test)

np.savetxt(RESULTADO, np.c_[range(1,len(test)+1),pred], delimiter=',', header = 'ImageId,Label', comments = '', fmt='%d')