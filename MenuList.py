import os
from menuss import Menu
from lista import Lista
from basicoo import Intermedio

opc = ""
while opc != "5":
    os.system("cls")
    men = Menu("Menú Principal",["1)Calculadora","2)Operación Números","3)Tratamiento de Listas","4)Operaciones de Cadenas","5)Salir"])
    opc = men.menu()

    if opc == "3":
        opc3 =""
        while opc3 != "11":
            os.system("cls") 
            men3 = Menu("Menú Tratamiento de Listas",["1)Recorrer y presentar los datos de una lista","2)Buscar un valor en una lista","3)Retornar una lista con los factoriales","4)Retornar una lista de números primos","5)Recorrer una lista de diccionario con notas de alumnos","6)Insertar un dato en una Lista dada lo Posición","7)Eliminar todas las ocurrencias en una Lista","8)Retornar cualquier valor de una lista eliminándolo ","9)Copiar cada elemento de una tupla en una lista","10)Dar el vuelto a varios clientes","11)Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
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
            elif opc3 == "2":
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
            elif opc3 == "3":
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
            elif opc3 == "4":
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
            elif opc3 == "5":
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
            elif opc3 == "6":
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
            elif opc3 == "7":
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
            elif opc3 == "8":
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
            elif opc3 == "9":
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
            elif opc3 == "10":
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