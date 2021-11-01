'''
    Proyecto 1 Programacion II
    Trabajo realizado por : Agustin Ascolani Y Marco Gregori


'''
'''         BIBLIOTECAS             
'''
import math
import functools
import json
import xml.etree.cElementTree as ET

'''         FUNCIONES              '''
def ProblemaFID():
    ''' XML '''
    raiz = ET.parse("Data.xml")
    UM = raiz.getroot()

    def DataUMnameXML(nombre):
        baseCS = raiz.findall(nombre + "/CantidadSensores")
        for elem in baseCS:
            CS = elem.text
            print("Cantidad de sensores en ", nombre, " : ", elem.text)
            print("-----------------------------------------------------")
        baseS = raiz.findall(nombre + "/Sensores")
        for child in baseS:
            for x in child:
                print(x.tag, " : ", x.text)
        if CS == "0":
            print("ERROR : Unidad Meterorologica Sin Sensores")
        print("-----------------------------------------------------")
        return None
    ''' JSON '''
    with open('Data.json', 'r',
              encoding="utf-8") as j:
        Data = json.load(j)

    Estaciones = Data["Estaciones"]

    def dataSensoresUM(nombre):
        sensores = (Estaciones[nombre]["Sensores"])
        cantidadSensores = (Estaciones[nombre]["CantidadSensores"])
        print("Cantidad de sensores en ", nombre, " : ", cantidadSensores)
        print("-----------------------------------------------------")
        for sensor in sensores:
            if "Humedad" in sensor:
                print("Humedad : ", sensor.get("Humedad"), "hma")
            elif "Temperatura" in sensor:
                print("Temperatura : ", sensor.get("Temperatura"), "C°")
            elif "Viento" in sensor:
                print("Viento : ", sensor.get("Viento"), "Km/h")
            else:
                print("ERROR : Unidad Meterorologica Sin Sensores")

        print("-----------------------------------------------------")

        return None

    def umMenorVoltaje():
        total = {}
        for Estacion in Estaciones:
            data = Estaciones[Estacion]["Bateria mV"]
            if data != []:

                promedio = sum(data) / len(data)

                total[Estacion] = promedio

            else:
                print('''AVISO : Unidad Meteorologica''', Estacion, '''sin una bateria funcional
                ''')

        total = (sorted(total.items(), key=lambda item: item[1]))
        print(""
              "Unidad meteorologica con menor bateria : ")
        print(min(total))
        print("")

        return None

        return None

    print('''
        
        Problema 1: A partir del nombre de la estación, computar la cantidad de sensores disponible y mostrar por pantalla
    los diferentes sensores, cada uno deberá mostrar el tipo y la variable medida:
    
    Lenguaje utilizado : (JSON)
    
    ''')
    nombre = input('''
    
    Nombre de Estaciones:
    
    -UM San Juan
    -UM Gral Roca
    -UM 9 de Julio
    -UM San Martin
    
    Inserte el nombre de una Estacion para tener más informacion sobre ella:
    '''

          )
    dataSensoresUM(nombre)
    eleccion = input('''Deseas seguir insertando nombres [1] o ir al siguiente prblema [0]?''')
    if eleccion == "1":
        ProblemaFID()
    elif eleccion == "0":

        print(''' Problema 2: Calcular cuál es la estación con menos batería, es decir, la estación con menor valor promedio de
voltaje.

Solucion:
''')
        umMenorVoltaje()
        eleccion2 = input("Desea ver el ejercicio siguiente (Formato XML) [1] o volver al menu [0]?:")
        if eleccion2 == "1":
            print('''A continuacion, podras buscar la informacion de una Unidad Meteorologica en base a su nombre,
             con la diferencia que esta en formato xml... ''')
            nombre = input('''

                Nombre de Estaciones:

                -UM_San_Juan
                -UM_Gral_Roca
                -UM_9_de_Julio
                -UM_San_Martin

                Inserte el nombre de una Estacion para tener más informacion sobre ella:
                '''

                           )
            DataUMnameXML(nombre)
            eleccion = input('''Desea ir al siguiente problema [1] o ir al menu [0]?''')
            if eleccion == "1":
                print('''No pudimos hacerlo... :( ''')
                eleccion2 = input('''Desea ir al comienzo de este problema [1] o ir al menu [0]?''')
                if eleccion2 == "1":
                    ProblemaFID()
                elif eleccion2 == "0":
                    ShowMenu()
                else:
                    print("Error")

            elif eleccion == "0":
                ShowMenu()

            else:
                print("Error")



        elif eleccion2 == "0":
            ShowMenu()
        else:
            print("Error")


    else:
        print("Error ")


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
            if x < 0:
                print("Error, inserte un numero mayor a cero")
                ShowMenu()
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
        eleccion2 = input("Desea volver a ver el primer ejercicio [1], volver al menu [0] o ver funciones para validar"
                          " ejercicios de ER (opcional) [2]:")
        if eleccion2 == "1":
            ProblemaRegex()
        elif eleccion2 == "0":
            ShowMenu()
        elif eleccion2 == "2":
            print(''' 
            en la librería estandar de Python podemos encontrar el módulo re,
            el cual nos proporciona todas las operaciones necesarias para trabajar con las expresiones regulares.
            Esta biblioteca tiene los siguientes métodos para buscar coincidencias con nuestro texto.
            
                -match(): determina si la regex tiene coincidencias en el comienzo del texto.
                -search(): escanea todo el texto buscando cualquier ubicación donde haya una coincidencia.
                -findall() encuentra todos los subtextos donde haya una coincidencia y
                 nos devuelve estas coincidencias como una lista.
                -finditer():similar al anterior pero en lugar de devolvernos 
                 una lista nos devuelve un iterador.
                 
                 A continuación veremos un ejemplo de la implementacion de una funcionalidad...
                 
                 Si quisieramos determinar si una patente del ejercicio 1 es válida podriamos utilizar la funcion match
                 , pero para eso primero debemos importar la biblioteca re...
                 
                 # Despues de eso, determinariamos el patron o expresion regular para modelo comparativo
                 
                 patron = re.compile(r'L[VQ]-[A-Z]\w{2,4}')
                 
                 # Luego determinaremos la patente a verificar...
                 
                 patente = "LV-QWE"
                 
                 # Finalmente comenzariamos el testeo imprimiendo la el resultado...
                 
                 print(patron.match(texto))
                 
                 El output de esto seria : <re.Match object; span=(0, 6), match='LV-QWE'>
                 
                 Basicamente expresa que encontro un objeto, con el patron especificado en el string especificado...
                    
                 ''')
            eleccion3 = input("Desea ver el ejercicio anterior [1], volver al menu [0] :")
            if eleccion3 == "1":
                ProblemaRegex()
            elif eleccion3 == "0":
                ShowMenu()
            else:
                    print("Error")
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
            ProblemaFID()
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