from menuss import Menu
from calculadora import Calculadora,CalCientifica,CalEstandar
from basicoo import Basico, Intermedio
from lista import Lista
from basicoo import Intermedio
from cadena import Cadena
import os        
opcion = ""  
while opcion != "5": 
    men= Menu("Menu Principal",["1) Calculadora","2) Numeros","3) Listas","4) Operaciones de cadenas","5) Salir"])
    opcion = men.menu()
    os.system ("cls")
    
    if opcion == "1":
        opci1=""
        while opci1 !="11":
            os.system ("cls")
            men = Menu("Menu Calculadora",  ["1) Suma", "2) Resta", "3) Multiplicacion", "4) Division", "5) Multiplicacion Estandar", "6) Exponente", "7) Valor Absoluto", "8) Circunferencia", "9) Area Circulo", "10) Area Cuadrado","11) Salir"])
            opci1 = men.menu()
            os.system ("cls")
    
    
            if opci1 == "1":
                print("Calculadora --- Suma")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print("{} + {} = {}".format(n1,n2,cal.suma()))
                input("presione una tecla para continuar")
                
                
            if opci1 == "2":
                print("Calculadora --- Resta")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print("{} - {} = {}".format(n1,n2,cal.resta()))
                input("presione una tecla para continuar")
            
            
            if opci1 == "3":
                print("Calculadora --- Multiplicacion")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print(cal.multiplicacion())
                input("presione una tecla para continuar")
                
            
            if opci1 == "4":
                print("Calculadora --- Divison")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print(cal.division())
                input("presione una tecla para continuar")         
                
            if opci1 == "5":
                print("Calculadora Estandar --- Multiplicacion")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                calest = CalEstandar(n1,n2)
                print("{} * {} = {}".format(n1,n2,calest.multiplicacion()))
                input("presione una tecla para continuar")
                
                
            if opci1 == "6":
                print("Calculadora Estandar --- Exponente")
                n1 = int(input("Ingrese el valor de la Base: "))
                n2 = int(input("Ingrese el valor del Exponente: "))
                calest = CalEstandar(n1,n2)
                print("{} ^ {} = {}".format(n1,n2,calest.exponente()))
                input("presione una tecla para continuar")    
                
                
            if opci1 == "7":
                print("Calculadora Estandar --- Valor Absoluto")
                n1 = int(input("Ingrese el valor: "))
                calest = CalEstandar(0,0)
                print("El valor absoluto es: {}".format(calest.valorAbsoluto(n1)))
                input("presione una tecla para continuar")    
                
            
            if opci1 == "8":
                print("Calculadora Ciencitifica --- Circunferencia")
                n1 = int(input("Ingrese el valor a calcular: "))
                calcie = CalCientifica(n1,0)
                print(calcie.circunferencia())
                input("presione una tecla para continuar")
                
                
            if opci1 == "9":
                print("Calculadora Cientifica --- Area de un Circulo")
                n1 = float(input("Ingrese el valor a calcular: "))
                calcie = CalCientifica(n1,0)
                print(calcie.areaCirculo())
                input("presione una tecla para continuar")
                
                
            if opci1 == "10":
                print("Calculadora Cientifica --- Area de un Cuadrado")
                n1 = int(input("Ingrese el valor del lado 1-2: "))
                n2 = int(input("Ingrese el valor del lado 3-4: "))
                calcie = CalCientifica(n1,n2)
                print(calcie.areaCuadrado())
                input("presione una tecla para continuar")
 
    if opcion == "2":
        opci1= ""
        while opci1 != "11":
            os.system ("cls")
            men= Menu("Menu Operacion numeros",["1) Numeros de 1 a n","2) Suma de 1 a n","3) Multiplo de numero","4) Divisores de un numero","5) Numero primo","6) Factorial de cualquier numero","7) Fibonacci serie de n numero","8) Perfecto","9) Primos gemelos","10) Numeros amigos","11) Salir"])
            opci1= men.menu()
            os.system ("cls")
        
            if opci1 == "1":
                print("NUMEROS DE 1 a n")
                Nnum = Basico()
                Nnum.numerosN()
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "2":
                os.system ("cls")
                print("Suma de 1 a n")
                sumN= Basico()
                sumN.numerosNsuma()
                input("Pulse cualquier tecla si desea continuar...")
            
            if opci1 == "3":
                os.system ("cls")
                print("Multiplo de numero")
                multi= Basico()
                multi.multiplo(())
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "4":
                os.system ("cls")
                print("Divisores de un numero")
                divi = Basico()
                print(divi.DivisoresNumero())
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "5":
                os.system ("cls")
                print("Numero primo")
                prim= Basico()
                prim.primo()
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "6":
                os.system ("cls")
                print("Factorial de un numero")
                Fact = Intermedio()
                Fact.factorial()
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "7":
                os.system ("cls")
                print("Fibonacci de numero")
                fibo= Intermedio()
                fibo.fibonacci()
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "8":
                os.system ("cls")
                print("Perfecto de numero")
                perfec= Basico()
                print(perfec.perfecto())
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "9":
                os.system ("cls")
                print("Primos gemelos")
                priGem= Intermedio()
                priGem.primosGemelos(())
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "10":
                os.system ("cls")
                print("Numeros amigos")
                ami= Intermedio()
                ami.amigos(())
                input("Pulse cualquier tecla si desea continuar...")
                
    if opcion == "3":
        opci1=""
        while opci1 != "11":
            os.system("cls") 
            men3 = Menu("Menú Tratamiento de Listas",["1)Recorrer y presentar los datos de una lista","2)Buscar un valor en una lista","3)Retornar una lista con los factoriales","4)Retornar una lista de números primos","5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo ","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
            opc3 = men3.menu()
            if opci1 == "1":
                os.system("cls")
                lista =[]
                cont = 0
                r= int(input("Digite la cantidad de elementos que va a tener su lista:"))
                while  r != cont:
                    q= str(input("Digite los datos que va a contener la lista: "))
                    lista.append(q)
                    cont +=1
                os.system("cls")
                print("Recorrer y presentar los datos de una lista")
                print("Lista =",lista)
                Lis = Lista(lista)
                Lis.presentarLista()
                input("Presione una tecla para continuar")
            elif opci1 == "2":
                os.system("cls")
                lista =[]
                cont = 0
                g = int(input("Digite la cantidad de elementos que va a tener la lista:"))
                while  g != cont:
                    q= str(input("Ingrese los datos que va a contener la lista: "))
                    lista.append(q)
                    cont +=1
                os.system("cls")
                print("Buscar un valor en una lista")
                print("Lista =",lista)
                Lis = Lista(lista)
                print(Lis.buscarLista())
                input("Presione una tecla para continuar")
            elif opci1 == "3":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Retornar una lista con los factoriales")
                print("Lista =",lista)
                Lis = Lista(lista)
                resultado= Lis.listaFactorial()
                input("Presione una tecla para continuar")
            elif opci1 == "4":
                os.system("cls")
                lista =[]
                cont = 0
                q = int(input("Ingrese la cantidad de elementos que va a tener la lista:"))
                while  q != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Retornar una lista de números primos")
                print("Lista =",lista)
                Lis = Lista(lista)
                resultado = Lis.listaPrimo()
                input("Presione una tecla para continuar")
            elif opci1 == "5":
                os.system("cls")
                print("Recorrer una lista de diccionario con notas de alumnos")
                li=[]
                di = {}
                cant = int(input('Ingrese el número de datos que va a tener el diccionario: '))
                for i in range(cant):
                    clave =input('Nombre del alumno: ')
                    valor =input('Nota del alumno: ')
                    di[clave] = valor
                li.append(di)
                print(di)
                Lis = Lista(li)
                Lis.listaNotas(di)
                input("Presione una tecla para continuar")
            elif opci1 == "6":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de elementos que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los datos que va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Insertar un dato en una Lista dada lo Posición")
                print("Lista =",lista)
                valor = int(input("Ingrese valor a agregar: "))
                posicion = int(input("Ingrese posicion: "))
                Lis = Lista(lista)
                Lis.insertarLista(valor, posicion)
                input("Presione una tecla para continuar")
            elif opci1 == "7":
                os.system("cls")
                lista =[]
                cont = 0
                x = int(input("Ingrese la cantidad de valores que va a tener la lista:"))
                while  x != cont:
                    y= str(input("Ingrese los valores de va a tener la lista: "))
                    lista.append(y)
                    cont +=1
                os.system("cls")
                print("Eliminar todas las ocurrencias en una Lista")
                lis= Lista(y)
                lis.eliminarLista(y)
                input("Presione una tecla para continuar")
            elif opci1 == "8":
                os.system("cls")
                lista =[]
                cont = 0
                q = int(input("Ingrese la cantidad de elementos que va a tener la lista:"))
                while  q != cont:
                    f= str(input("Ingrese los datos de va a tener la lista: "))
                    lista.append(f)
                    cont +=1
                os.system("cls")
                print("Retornar cualquier valor de una lista eliminándolo ")
                print("Lista =",lista)
                posicion = int(input("Eliminar posicion: "))
                Lis = Lista(lista)
                print("El número que se encontraba en la posicion {} es {} y la lista quedo de la siguiente forma {} ".format(posicion,lista[posicion],Lis.retornaValorLista(posicion)))
                input("Presione una tecla para continuar")
            elif opci1 == "9":
                os.system("cls")
                print("Copiar cada elemento de una tupla en una lista")
                tupla,cont = (), 0
                nun = int(input("Ingrese el número de datos que desea que tenga su tupla: "))
                while cont != nun:
                    valor = str(input("Ingrese el valor que desea que este en su tupla: "))
                    tupla = tupla + (valor,)
                    cont +=1
                print("Tupla: ",tupla)
                Lis = Lista("NADA")
                print("Lista: ",Lis.copiarTuplaLista(tupla))
                input("Presione una tecla para continuar")
            elif opci1 == "10":
                os.system("cls")
                print("Dar el vuelto a varios clientes")
                li=[]
                di = {}
                cant = int(input('Ingrese el número de datos que va a tener el diccionario: '))
                for i in range(cant):
                    clave =input('Nombre del cliente: ')
                    valor =input('vuelto del cliente $: ')
                    di[clave] = valor
                li.append(di)
                print(di)
                Lis = Lista(li)
                Lis.vueltoLista(di)
                input("Presione una tecla para continuar")
            elif opc3 == "11":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")          
                          
                
    if opcion == "4":
        opc4 =""
        while opc4 != "10":
            os.system("cls") 
            men4 = Menu("Menú Operaciones de Cadenas",["1) Recorrer y presentar los datos de una cadena", "2) Buscar un carácter en una cadena", "3) Retornar una lista con la posiciones dado un carácter de la cadena", "4) Retornar una lista con todas las palabras de una cadena", "5) Retornar una cadena a partir de una lista", "6) Insertar un dato en una cadena dada lo Posición", "7) Eliminar todas las ocurrencias en una cadena", "8) Retornar cualquier valor de una cadena eliminándolo ", "9) Concatenar cadenas", "10) Salir"])
            opc4 = men4.menu()
            
            
            if opci1 == "1":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Recorrer y presentar los datos de una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                Cad = Cadena(cadena)
                Cad.recorrerCadena()
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "2":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Buscar un carácter en una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                buscar = str(input("Ingrese el caracter que desea buscar: "))
                Cad = Cadena(cadena)
                print(Cad.buscarCaracter(buscar))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "3":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                caracter = str(input("Ingrese el caracter que desea buscar: "))
                Cad = Cadena(cadena)
                print(Cad.listaPosiciones(caracter))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "4":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar una lista con todas las palabras de una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                Cad = Cadena(cadena)
                print(Cad.listaPalabras())
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "5":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar una cadena a partir de una lista")
                lista =[]
                cont =0
                x =int(input("Ingrese la cantidad que desea que tenga la lista: "))
                while x != cont:
                    y = input("Ingrese los datos para la lista: ")
                    lista.append(y)
                    cont +=1
                print("Lista: ",lista)
                Cad = Cadena("NADA")
                print("Cadena: ",Cad.cadenaLista(lista))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "6":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Insertar un dato en una cadena dada lo Posición")
                cadena = str(input("Ingrese una o más variables de texto: "))
                dato = input("Ingrese el dato que va a ingresar a la cadena: ")
                posicion = int(input("Ingrese la posicion donde va a colocar el dato: "))
                Cad = Cadena(cadena)
                print(Cad.insertarDato(dato, posicion))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "7":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Eliminar todas las ocurrencias en una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                buscar = str(input("Ingrese la ocurrencia que desea eliminar: "))
                Cad = Cadena(cadena)
                print(Cad.eliminarOcurrencias(buscar))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "8":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar cualquier valor de una cadena eliminándolo ")
                cadena = str(input("Ingrese una o más variables de texto: "))
                posicion = int(input("Ingrese la posición donde se encuntre el caracter: "))
                Cad = Cadena(cadena)
                print(Cad.retornaValor(posicion))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "9":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Concatenar cadenas")
                cadena = str(input("Ingrese una o más variables de texto: "))
                dato = str(input("Ingrese lo que va a concatenar a la cadena: "))
                Cad = Cadena(cadena)
                print(Cad.concatenarCadena(dato))
                input("Presione una tecla para continuar")
                
                
            elif opci1 == "10":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
                
                
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")
                
                
    
                    
print("Muchas gracias por su visita, vuelva cuando quiera")
            
        
        
        
    