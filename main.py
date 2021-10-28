'''
    Proyecto 1 Programacion II
    Trabajo realizado por : Agustin Ascolani Y Marco Gregori


'''
'''         BIBLIOTECAS             
'''
import math
import functools



'''         FUNCIONES              '''

def ProblemaColecciones():
    print('''
    Problema  1: Explicar en pocas palabras y utilizando diagramas las operaciones de map, filter y reduce. Proponga
    ejemplos de cada uno (conceptuales, no necesariamente en código).

    Solucion: Esta en el archivo "Colecciones 1.pdf"
    ''')
    eleccion = input("Desea ver el siguiente problema [1] o volver al menu [0]?:")
    if eleccion == "1":

        print('''
        Problema 2: El número irracional “pi” puede calcularse a partir una serie, Implemente un algoritmo
         sin usar estructuras repetitivas para calcular una aproximación de pi con N
        términos.:
        
                ''')
        lista = []
        def CrearRangoSerie(x):
            if x == 0:
                lista.append(x)

            else:
                lista.append(x)
                x = x - 1
                CrearRangoSerie(x)
            lista.sort()
            return lista
        def CalculoSerie(i):
            numerador = 4 * pow(-1, i)
            denominador = (2 * i + 1)
            resultado = numerador / denominador

            return resultado
        def Suma(a, b):
            return a + b
        RangoMax = int(input("  Inserte el numero limite de la serie, mientras mayor sea, más"
                         "se acercara al numero Pi, tenga en cuenta que el máximo es 994 "))
        lista = CrearRangoSerie(RangoMax)
        MapeoLista = map(CalculoSerie, lista)
        print("Resultado de la serie : ")
        print(functools.reduce(Suma, list(MapeoLista)))
        print('''Si desea saber más acerca de esta serie googlé "serie Gregory-Leibniz"''')


        eleccion2 = input("Desea ver el ejercicio anterior [1] o volver al menu [0]?:")
        if eleccion2 == "1":
            ProblemaColecciones()
        elif eleccion2 == "0":
            ShowMenu()
        else:
            print("Error")

    elif eleccion == "0":
        ShowMenu()
    else:
        print("Error ")

def ProblemaRegex():
    print('''
    Problema 1 : Las matrículas de las aeronaves en Argentina tienen el siguiente formato de acuerdo a su tipo (donde
    abc significa 3 letras mayúsculas y 123 3 dígitos):

    Solución: "L[VQ]-[A-Z]\w{2,4}"

''')
    eleccion = input("Desea ver el siguiente problema [1] o volver al menu [0]?:")
    if eleccion == "1":
        print('''
        Problema 2 : Diseñe una ER para validar cadenas de números naturales menores a 1900.

        Solucion: "^([1-9][0-9]{0,2}|[1][0-8][0-9][0-9]|[-][0-9]*)$" }
        ''')
        eleccion2 = input("Desea ver el ejercicio anterior [1] o volver al menu [0]?:")
        if eleccion2 == "1":
            ProblemaRegex()
        elif eleccion2 == "0":
            ShowMenu()
        else:
            print("Error")

    elif eleccion == "0":
        ShowMenu()
    else:
        print("Error ")


def ShowMenu():
    res = True
    while (res == True):
        print('''
                Bienvenido al menu del Proyecto N°1!!

                Selecciona que problema desea observar...

                1-Problemas de Expresiones Regulares
                2-Problemas de Recursividad
                3-Problemas de Colecciones
                4-Problemas de Formato intercambio de datos
                5-Salir
                ''')
        eleccion = input("Ingrese los problemas que desees ver... ")
        if eleccion == '1':
            ProblemaRegex()
        elif eleccion == '2':
            print("a")
        elif eleccion == '3':
            ProblemaColecciones()
        elif eleccion == '4':
            print("a")
        elif eleccion == '5':
            print("Adios")
            res = False
        else:
            print("Ingrese un parametro valido")
            ShowMenu()

        return None


'''
        LLAMADO A FUNCIONES 
'''
ShowMenu()