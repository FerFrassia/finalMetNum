import random

preguntas = {
	"EG": ["Costo?"],
	"LU": ["Toda matriz tiene LU?, de qu ́e depende?", "Conocés alguna condición si y sólo si para que tenga LU (aparte de la de eliminación Gaussiana)?", "Qué problema tengo si hago eliminación gaussiana con pivoteo para conseguir LU?", "Cuando la factorización LU es única?", "Por qué queremos pivotear en EG aunque no tengamos necesidad?"],
	"Número de condición y normas": ["Qué es el número de condición? Intuición y definición"],
	"Cholesky": ["Para qué sirve?", "Si una matriz es SDP) ¿cómo te conviene resolver un sistema lineal?", "Ventajas de tener la factorizacion de Cholesky contra LU?", "La Factorización Cholesky es única?"],
	"QR": ["Toda matriz tiene factorización QR? Nombrar un método", "Es única? Bajo qué condiciones lo es?", "Para qué sirve?", "Idea de cómo se obtiene con rotaciones y reflexiones", "Cuál conviene mejor, Givens o Householder?"],
	"Autovalores": ["Cuántos autovalores tiene una matriz?", "Si para cada autovalor hay un autovector, tengo n autovectores?", "Dar alguna condición para afirmar que tenemos una base de autovectores.", "Algún método para encontrar el autovalor más grande de una matriz", "Qué condiciones son necesarias para que el método de la potencia converja?", "Qué condiciones son necesarias para aplicar el método de deflación?"],
	"SVD": ["Qué tamaño tiene cada matriz en la descomposición?", "Qué son los valores singulares?", "Cómo sé que los puedo obtener?", "Qué son las columnas de U y las columnas de V?", "Por qué podemos asegurar que $AA^t$ y $A^tA$ tienen base de autovectores?"],
	"Métodos iterativos": ["Por qué usaría métodos iterativos si tengo métodos exactos?", "Explicar Jacobi", "Explicar Gauss-Sidel", "Cuándo convergen? Condiciones necesarias y suficientes", "Características de algún método iterativo que te sirva si A es SDP", "Qué es el radio espectral?"],
	"CML": ["Qué problema resuelve?", "Cómo llevo este problema a una representación matricial?", "Por qué está bueno cuadrados mínimos lineales en relación a cuadrados mínimos no lineales?", "Por qué decimos que CML es lineal?¿Por qué está bueno usar CML en comparación a no lineales?", "Interpretación geométrica?", "Tengo un problema de cuadrados mínimos, siempre tiene solución?¿Es única?", "Qué métodos conocés para resolver cuadrados mínimos?", "Interpolar vs Aproximar", "Criterios para definir mejor aproxima"],
	"Interpolación": ["Quiero dar un polinomio interpolador. ¿Siempre existe?¿Es único? ¿Qué algoritmos conoces para calcularlo?", "Qué problemas trae tener un polinomio interpolante de grado muy alto?¿Solución?", "Qué es un polinomio interpolador?", "Fórmula del error", "Cómo demostrás que el polinomio interpolador es único?"],
	"Existencia y unicidad": ["EG", "LU", "PLU", "Cholesky", "QR", "Givens", "Householder", "Potencia", "Deflación", "SVD", "Jacobi", "Gauss-Sidel", "CML", "Interpolación"]
}

def tomarFinal():
	categorias = list(preguntas.keys())
	print("Comencemos ;)")
	while(len(categorias) != 0):
		categoria = random.choice(categorias)
		categorias.remove(categoria)

		var = input("")
		print("Categoría: " + str(categoria))

		preguntasDeEstaCategoria = preguntas[categoria]
		while(len(preguntasDeEstaCategoria) != 0):
			pregunta = random.choice(preguntasDeEstaCategoria)
			preguntasDeEstaCategoria.remove(pregunta)
			var = input("")
			print(pregunta)

tomarFinal()