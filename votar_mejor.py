A1 = "submission_trans2.csv"
A2 = "submission_trans.csv"
A3 = "submission.csv"

submissions = [A1,A2,A3]

def votar():

	archivos = [open(sub) for sub in submissions]
	resultado = open("submission","w")

	lineas = [f.readline() for f in archivos]


	lineas = [f.readline() for f in archivos]

	while lineas[0]:
		
		
		lineas = [f.readline() for f in archivos]



	for f in archivos:
		f.close()
	resultado.close()

def getClase(l):
	return l.split(",")[1]

def getClases(l1,l2,l3):
	return getClase(l1), getClase(l2), getClase(l3)

def comparar(a,b,c):
	if (a != b or b != c or a != c):
		print ( '%d-%d-%d' % (int(a), int(b), int(c)) )

if __name__ == '__main__':
 votar()