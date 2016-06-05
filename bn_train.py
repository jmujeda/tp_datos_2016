
import csv

#Este programa convierte las imágenes del set de entrenamiento a blanco y negro, convertí los menores de 20 a 0 y el resto a 255


TRAIN = "train.csv"
TRAIN_BN = "train_bn.csv"

def run():
	f = open(TRAIN)
	fOutput = open(TRAIN_BN,"a")
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
			if (int(elem) < 20):
				vPixeles[j] = 0
			else:
				vPixeles[j] = 255
					
		wr.writerow(vPixeles)
	f.close()
	fOutput.close()

run()