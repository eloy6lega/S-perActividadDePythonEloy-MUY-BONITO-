# EJERCICIO 2
# Notas: HitoI 30% HitoG 20% Examen50%

#Entradas declaradas como nota1, nota2, nota3
#El proceso y la salida los he fusionado en el print de las líneas 10, 13, 16.
#El proceso final es la línea 19 (notaTotal)
#La salida final es la línea 20 (print)

def notas():

    nota1=float(input('¿Que nota has sacado en el Hito Individual?: '))
    print(f'En la nota consta como un: {nota1*0.3}')

    nota2=float(input('¿Que nota has sacado en el Hito Grupal?: '))
    print(f'En la nota consta como un: {nota2*0.2}')

    nota3=float(input('¿Que nota has sacado en el Examen?: '))
    print(f'En la nota consta como un: {nota3*0.5}')

    notaTotal=nota1*0.3+nota2*0.2+nota3*0.5
    print(f'La nota final es: {notaTotal}')

notas()

#EJERCICIO 3
# • Se pide calcular la nota de tu examen tipo test.
# • Serán 20 preguntas
# • Las preguntas correctas sumarán 0,5
# • Las preguntas incorrectas restarán 0,25
# • Las preguntas sin contestar tendrán 0
def calcularNotaTest():
    #DECORADOR
    print('---------------------------------------------------------------------------------------------------------------')
    print('BIENVENIDO A LA CALCULADORA DE TESTSANDGO.COM SIGA LOS PASOS A CONTINNUACIÓN')
    print('---------------------------------------------------------------------------------------------------------------')

    #Entrada
    print('El tipo Test consta de 20 preguntas. Una vez realizado, nos dirás cuántas preguntas has contestado en blanco, cuantas has acertado, y cunatas has fallado. Nosotros te daremos tu nota final :)')

    #Proceso / Conversion de entrada a entero (int)
    A=int(input('Aciertos: '))
    F=int(input('Fallos: '))
    B=int(input('En blanco: '))
    #Conversión de los datos
    NumPreguntas=A+F+B
    CalculatedA=A*0.5
    CalculatedF=F*0.25
    CalculatedB=B*0
    if NumPreguntas==20:
        #Operaciones de cálculo
        NotaTestCalculada=CalculatedA-CalculatedF+CalculatedB
        #Salida
        print(f'Tu nota del test es de: {NotaTestCalculada} puntos')
    else:
        print('No has introducido un total de 20 preguntas. Introduzca una suma de 20 y le daremos el resultado.')
calcularNotaTest()

#EJERCICIO 4
# • Diseña un algoritmo y un diagrama de flujo para:
# • Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y su área

#ENTRADA
#   creamos una clase llamada rectángulo con dos metodos para el perimetro y el area
#   las clases se crearan con un constructor

#DATOS:
#     nos pide la base del rectánculo
#     nos pide la altura del rectángulo

#OPERACIONES
#     calculamos el perimetro con una funcion de lado+lado+base+base o lo que es lo mismo lado*2+base*2

#SALIDA
#    Hacemos un print de los resultados de las variables anteriores

class Rectangulo():
    def __init__(self):
        self.base = int(input('dime la base del rectángulo: '))
        self.altura = int(input('dime la altura del rectángulo: '))
    def calcularPerimetro(self):
        print(f'el perimetro es {(self.base * 2) + (self.altura * 2)}')

    def calcularArea(self):
        print(f'el area es {self.base * self.altura}')


rectangulo1 = Rectangulo()
rectangulo1.calcularPerimetro()
rectangulo1.calcularArea()