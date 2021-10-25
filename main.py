'''
    Proyecto 1 Programacion II
    Trabajo realizado por : Agustin Ascolani Y Marco Gregori


'''


'''         FUNCIONES              '''

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
            print("a")
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