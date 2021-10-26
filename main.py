'''
    Proyecto 1 Programacion II
    Trabajo realizado por : Agustin Ascolani Y Marco Gregori


'''


'''         FUNCIONES              '''


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
            print("a")
        elif eleccion == '4':
            print("a")
        elif eleccion == '5':
            print("Adios")
            break
        else:
            print("Ingrese un parametro valido")
            break

        return None


'''
        LLAMADO A FUNCIONES 
'''
ShowMenu()