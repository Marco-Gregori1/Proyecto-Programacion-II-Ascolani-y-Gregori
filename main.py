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
    raiz = ET.parse("/Data.xml")
    UM = raiz.getroot()

    def NivelBatXML():
        Dicc = {}
        promedios = []
        for Estaciones in UM:
            total = []
            Estacion = (Estaciones.tag)
            for x in range(0, 20):
                valores = int(raiz.findall(Estacion + "/Bateria_mV")[x].text)
                total.append(valores)
            promedios = sum(total) / 20
            Dicc[Estacion] = promedios
        Dicc = (sorted(Dicc.items(), key=lambda item: item[1]))
        print("")
        print("Unidad Meteorologica con menor nivel de bateria : ", Dicc[0])
        print("")
        return None

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
        print(total)
        print("")
        print(""
              "Unidad meteorologica con menor bateria : ")

        print(total[0])
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
    
    - UM San Juan
    - UM Gral Roca
    - UM 9 de Julio
    - UM San Martin
    
    Inserte el nombre de una Estacion para tener más informacion sobre ella:
    '''

          )
    dataSensoresUM(nombre)
    eleccion = input('''Deseas seguir insertando nombres [1] o ir al siguiente problema [0]?''')
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

                - UM_San_Juan
                - UM_Gral_Roca
                - UM_San_Martin

                Inserte el nombre de una Estacion para tener más informacion sobre ella:
                '''

                           )
            DataUMnameXML(nombre)
            eleccion = input('''Desea ir al siguiente problema [1] o ir al menu [0]?''')
            if eleccion == "1":
                NivelBatXML()
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

def ProblemaRecursivo():
	def parimpar(cifra):
		if len(cifra) == 0:
			return cifra
		else:
			primera	= int(cifra[0])
			if primera % 2 == 0:
				return "1" + parimpar(cifra[1:])
			else:
				return "2" + parimpar(cifra[1:])

	def juntar_listas(listainter):
		if len(listainter) == 0:
			return listainter 
		else:
			return listainter[0]  + juntar_listas(listainter[1:])

	L = [ [1, 2, 3], [4, 5, 6], [7], [8] ]

	def iguales(listaUno, listaDos):
		if len(listaUno) != len(listaDos):
			return False
		elif len(listaUno) == 0 and len(listaDos) == 0:
			return True
		elif listaUno[0] == listaDos[0]:
			return iguales(listaUno[1:], listaDos[1:])
		else: 
			return False


	def dividir (dividendo, divisor):
		if divisor==0:
			return False
		elif dividendo == divisor:
			return 1
		elif dividendo < divisor:
			return 0
		else:
			return 1 + dividir(dividendo - divisor, divisor)
	print('''
	Consigna:
	Codificar un número entero de la siguiente manera cada dígito par sustituirlo por 1, cada dígito impar
por 2. Puede pasar el número a otras representaciones para resolver el ejercicio.
Ejemplo: El número 46579222 deberá codificarse como 11222111.

	''')
	print( 'Numero original :46579222')
	print ('Numero modificado: ',parimpar('46579222') )
	

	print('''
	---------------------------------------------
	
	Consigna:
	Convertir una lista de listas en una sola lista que tenga todos los elementos de las listas originales.
Ejemplo: Si L = [ [1, 2, 3], [4, 5, 6], [7], [8] ] la lista resultante deberá ser L2 = [1,2,3,4,5,6,7,8]


	''')
	print('Lista a unir :[ [1, 2, 3], [4, 5, 6], [7], [8] ] ')
	print('Lista Unida:')
	L = [ [1, 2, 3], [4, 5, 6], [7], [8] ]

	print(juntar_listas(L))


	print('''
	---------------------------------------------
	
	Consigna:
	 Decidir si dos listas de números enteros son iguales.

	''')
	print('''
	Listas a comparar:

	L  = [1, 2, 3, 4]
	L2 = [1, 2, 3, 8]
	L3 = [1, 2, 3, 8, 5]
	''')
	L  = [1, 2, 3, 4]
	L2 = [1, 2, 3, 8]
	L3 = [1, 2, 3, 8, 5]
	L4 = [1, 2, 3, 4]
	print('Ejemplo comparacion L3 y L2')
	print(iguales(L3,L2))
	print('Ejemplo comparacion L y L2')
	print(iguales(L,L2))
	print('Ejemplo comparacion L y L4')
	print(iguales(L,L4))


	print('''
	----------------------------
	
	Consigna:
	Realizar la división entera entre dos números enteros positivos A y B, (B ≠ 0). Ayuda: Pensar la
división entera como sucesión de restas


	''')
	
	print(' Aqui hay 3 resultados distintos, el primero funciona correcto, el segundo no se puede y el tercero da 0')
	print('6/3 = {}'.format(dividir(6, 3)))
	print('7/0 = {}'.format(dividir(7, 0)))
	print('1/9 = {}'.format(dividir(1, 9)))









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
            ProblemaRecursivo()
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