import csv
import timeit

#Este programa convierte las imagenes del set de entrenamiento a blanco y negro, converti los menores de 20 a 0 y el resto a 255


TRAIN = "train.csv"
TRAIN_BN = "bn_" + TRAIN
TEST = "test.csv"
TEST_BN = "bn_" + TEST

def bn_transformar(input, output):

	print "Transformando " + input 
	a = timeit.default_timer()

	f = open(input)
	fOutput = open(output,"w")
	wr = csv.writer(fOutput, quoting=csv.QUOTE_NONE)
	i = -1

	for linea in f:
		i += 1
		if (i == 0): #salteo el encabezado
			fOutput.write(linea)
			continue
		vPixeles = linea.split(',')

		j = -1
		for elem in vPixeles:
			j += 1
			if (j == 0):
				continue
			if (int(elem) < 60):
				vPixeles[j] = 0
			else:
				vPixeles[j] = 255
					
		wr.writerow(vPixeles)
	f.close()
	fOutput.close()

	b = timeit.default_timer()
	secs = b - a
	m, s = divmod(secs,60)
	m = int(m)
	s = int(s)
	print "Fin (" + str( m) + ":" + str(s ) + ")"

if __name__ == '__main__':
	bn_transformar(TRAIN, TRAIN_BN)
	bn_transformar(TEST, TEST_BN)