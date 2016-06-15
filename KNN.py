#el submit por defecto dio 0.96557 y tardo unos 20 minutos
#parametros usados: (k_neighbors = 10, algorithm = 'auto', n_jobs = 4)
#
#Para k=4, el score fue 0.96900
#knn1 sobre set BN = 0.96471
#!/usr/bin/python


from sklearn import neighbors
import csv
import numpy as np
import timeit


TRAIN = "train_bn.csv"
TEST = "test_bn.csv"
OUTPUT = "submissionknn.csv"

def knn(TRAIN, TEST, OUTPUT):
    print "Aplicando KNN " + TRAIN + " -> " + TEST 

    a = timeit.default_timer()

    with open(TRAIN, 'rb') as f:
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

    with open(TEST, 'rb') as f:
        reader = csv.reader(f)
        X_test = []

        for row in reader:
            if reader.line_num > 1:
                X_test.append(row)

        X_test = np.array(X_test)

    k_neighbors = 1
    clf = neighbors.KNeighborsClassifier(k_neighbors, algorithm = 'auto', n_jobs = 4)
    clf.fit(X, Y)

    Z = clf.predict(X_test)

    with open(OUTPUT, 'a') as f:
        header = 'ImageId,Label\n'
        f.write(header)
        ImageId = 0
        for prediction in Z:
            ImageId += 1
            line = str(ImageId) + ',' + str(prediction) + '\n'
            f.write(line)

    b = timeit.default_timer()
    secs = b - a
    m, s = divmod(secs,60)
    m = int(m)
    s = int(s)
    print "Fin (" + str( m) + ":" + str(s ) + ")"

if __name__ == '__main__':
    knn(TRAIN, TEST, OUTPUT)