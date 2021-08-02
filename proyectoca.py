import os
from cadena import Cadena
from menuss import Menu

opc = ""
while opc != "5":
    os.system("cls")
    men = Menu("Menú Principal",["1)Calculadora","2)Operación Números","3)Tratamiento de Listas","4)Operaciones de Cadenas","5)Salir"])
    opc = men.menu()
    
    
    if opc == "4":
        opc4 =""
        while opc4 != "10":
            os.system("cls") 
            men4 = Menu("Menú Operaciones de Cadenas",["1) Recorrer y presentar los datos de una cadena", "2) Buscar un carácter en una cadena", "3) Retornar una lista con la posiciones dado un carácter de la cadena", "4) Retornar una lista con todas las palabras de una cadena", "5) Retornar una cadena a partir de una lista", "6) Insertar un dato en una cadena dada lo Posición", "7) Eliminar todas las ocurrencias en una cadena", "8) Retornar cualquier valor de una cadena eliminándolo ", "9) Concatenar cadenas", "10) Salir"])
            opc4 = men4.menu()
            
            
            if opc4 == "1":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Recorrer y presentar los datos de una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                Cad = Cadena(cadena)
                Cad.recorrerCadena()
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "2":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Buscar un carácter en una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                buscar = str(input("Ingrese el caracter que desea buscar: "))
                Cad = Cadena(cadena)
                print(Cad.buscarCaracter(buscar))
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "3":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar una lista con la posiciones dado un carácter de la cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                caracter = str(input("Ingrese el caracter que desea buscar: "))
                Cad = Cadena(cadena)
                print(Cad.listaPosiciones(caracter))
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "4":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar una lista con todas las palabras de una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                Cad = Cadena(cadena)
                print(Cad.listaPalabras())
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "5":
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
                
                
            elif opc4 == "6":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Insertar un dato en una cadena dada lo Posición")
                cadena = str(input("Ingrese una o más variables de texto: "))
                dato = input("Ingrese el dato que va a ingresar a la cadena: ")
                posicion = int(input("Ingrese la posicion donde va a colocar el dato: "))
                Cad = Cadena(cadena)
                print(Cad.insertarDato(dato, posicion))
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "7":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Eliminar todas las ocurrencias en una cadena")
                cadena = str(input("Ingrese una o más variables de texto: "))
                buscar = str(input("Ingrese la ocurrencia que desea eliminar: "))
                Cad = Cadena(cadena)
                print(Cad.eliminarOcurrencias(buscar))
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "8":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Retornar cualquier valor de una cadena eliminándolo ")
                cadena = str(input("Ingrese una o más variables de texto: "))
                posicion = int(input("Ingrese la posición donde se encuntre el caracter: "))
                Cad = Cadena(cadena)
                print(Cad.retornaValor(posicion))
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "9":
                os.system("cls")
                print("Menu --- Operaciones de Cadenas")
                print("Concatenar cadenas")
                cadena = str(input("Ingrese una o más variables de texto: "))
                dato = str(input("Ingrese lo que va a concatenar a la cadena: "))
                Cad = Cadena(cadena)
                print(Cad.concatenarCadena(dato))
                input("Presione una tecla para continuar")
                
                
            elif opc4 == "10":
                print("Gracias por usar el sistema")
                input("Presione una tecla para continuar")
                
                
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")
                
                
    elif opc == "5":
        print("Espero que le haya sido de utilidad nuestro programa")
        print("Muchas gracias, vuelva pronto")
        
        
    else:
        print("Opción no valida")
        input("Presione una tecla para continuar")