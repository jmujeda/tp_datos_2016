import timeit

A1 = "submission8R.csv"
A2 = "submission_bn_8r.csv"
A3 = "submissionknn1_bn.csv"
A4 = "submissionknn1.csv" #MEJOR predictor

submissions = [A1,A2,A3,A4]

I_MEJOR = 3 #indice del mejor predictor
OUTPUT = "preddicion.csv"

def democratizar(submissions, OUTPUT , I_MEJOR):

	print "Democratizando los resultados"
	a = timeit.default_timer()

	archivos = [open(sub) for sub in submissions]
	resultado = open(OUTPUT,"w")

	lineas = [f.readline() for f in archivos]
	resultado.write(lineas[0])

	lineas = [f.readline() for f in archivos]

	while lineas[0]:
		k = elegir_mejor(lineas, I_MEJOR)
		i = getIndice(lineas[0]) #nro de imagen
		
		lineas = [f.readline() for f in archivos]
		resultado.write(i + "," + k + "\n")		

	for f in archivos:
		f.close()
	resultado.close()

	b = timeit.default_timer()
	secs = b - a
	m, s = divmod(secs,60)
	m = int(m)
	s = int(s)

	print "Fin (" + str( m) + ":" + str(s ) + ")"

	print "Submit: " + OUTPUT


#Calcula la mejor prediccion para la imagen
def elegir_mejor(vLineas, I_MEJOR):
	
	contadorPredicciones = {}
	for linea in vLineas:
		k = getClase(linea)
		if k in contadorPredicciones:
			contadorPredicciones[k] += 1
		else: 
			contadorPredicciones[k] = 1
	
	results = []
	for k in contadorPredicciones:
		results.append( (contadorPredicciones[k],k) )
	results = sorted(results,reverse=True)

	if len(results) == 1:
		return results[0][1]
	elif results[0][0] == results[1][0]: #hay empate
		return getClase(vLineas[I_MEJOR])
	else:
		return results[0][1]


def getIndice(l):
	return l.split(",")[0]

def getClase(l):
	return l.split(",")[1].rstrip()

def getClases(l1,l2,l3):
	return getClase(l1), getClase(l2), getClase(l3)

if __name__ == '__main__':
	democratizar(submissions, OUTPUT, I_MEJOR)