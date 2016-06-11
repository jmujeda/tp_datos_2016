#el submit por defecto dio 0.96557 y tardo unos 20 minutos
#parametros usados: (k_neighbors = 10, algorithm = 'auto', n_jobs = 4)
#
#Para k=4, el score fue 0.96900
#!/usr/bin/python
from sklearn import neighbors
import csv
import numpy as np

print "reading training data"

with open('train.csv', 'rb') as f:
    reader = csv.reader(f)
    X = []
    Y = []

    for row in reader:
        if reader.line_num > 1:
            X.append(row[1:])
            Y.append(row[0])

    #X = 784 x N, Y = N
    X = np.array(X)
    Y = np.array(Y)

print "reading test data"

with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    X_test = []

    for row in reader:
        if reader.line_num > 1:
            X_test.append(row)

    X_test = np.array(X_test)

print "fitting model"

k_neighbors = 1
clf = neighbors.KNeighborsClassifier(k_neighbors, algorithm = 'auto', n_jobs = 4)
clf.fit(X, Y)

print "making predictions"

Z = clf.predict(X_test)

print "writing predictions to file"

with open('submissionknn1.csv', 'w+') as f:
    header = 'ImageId,Label\n'
    f.write(header)
    ImageId = 0
    for prediction in Z:
        ImageId += 1
        line = str(ImageId) + ',' + str(prediction) + '\n'
        f.write(line)