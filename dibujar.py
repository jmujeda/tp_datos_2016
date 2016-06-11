
import Image
import ImageFilter as imgF

ARCHIVO = "test.csv"

def exportar():
	f = open(ARCHIVO)
	i = -1

	for linea in f:
		
		i += 1
		if	(i == 0):
			continue
		if (i == 500):
			break
		linea = linea.split(",")
		num = linea[0]
		dibujar( linea[1:len(linea) - 1], str(num) + "_" + str(i) + ".png")
	f.close()
	return

def dibujar(vPixeles,nombre):
	
	for x in range (0,len(vPixeles)):
		vPixeles[x] =  int(vPixeles[x])

	im = Image.new('L', (28, 28))
	im.putdata(vPixeles)
	im = im.filter(imgF.SHARPEN)
	
	im.save('imagenes_test/' + nombre, format='png', subsampling=0, quality=100)
	return

exportar()