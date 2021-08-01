from menuss import Menu
from calculadora import Calculadora, CalEstandar, CalCientifica
import os
opcion=""
while opcion != "5": 
    men= Menu("Menu Principal",["1) Calculadora","2) Numeros","3) Listas","4) Operaciones de cadenas","5) Salir"])
    opcion = men.menu()
    os.system ("cls")

    if opcion == "1":
        op1=""
        while op1 !="11":
            os.system ("cls")
            men = Menu("Menu Calculadora",  ["1) Suma", "2) Resta", "3) Multiplicacion", "4) Division", "5) Multiplicacion Estandar", "6) Exponente", "7) Valor Absoluto", "8) Circunferencia", "9) Area Circulo", "10) Area Cuadrado","11) Salir"])
            op1 = men.menu()
            os.system ("cls")
            
            if op1 == "1":
                print("Calculadora --- Suma")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print("{} + {} = {}".format(n1,n2,cal.suma()))
                input("presione una tecla para continuar")
                
                
            if op1 == "2":
                print("Calculadora --- Resta")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print("{} - {} = {}".format(n1,n2,cal.resta()))
                input("presione una tecla para continuar")
            
            
            if op1 == "3":
                print("Calculadora --- Multiplicacion")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print(cal.multiplicacion())
                input("presione una tecla para continuar")
                
            
            if op1 == "4":
                print("Calculadora --- Divison")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                cal = Calculadora(n1,n2)
                print(cal.division())
                input("presione una tecla para continuar")
                
                
            if op1 == "5":
                print("Calculadora Estandar --- Multiplicacion")
                n1 = int(input("Ingrese el Primer valor: "))
                n2 = int(input("Ingrese el Segundo valor: "))
                calest = CalEstandar(n1,n2)
                print("{} * {} = {}".format(n1,n2,calest.multiplicacion()))
                input("presione una tecla para continuar")
                
                
            if op1 == "6":
                print("Calculadora Estandar --- Exponente")
                n1 = int(input("Ingrese el valor de la Base: "))
                n2 = int(input("Ingrese el valor del Exponente: "))
                calest = CalEstandar(n1,n2)
                print("{} ^ {} = {}".format(n1,n2,calest.exponente()))
                input("presione una tecla para continuar")    
                
                
            if op1 == "7":
                print("Calculadora Estandar --- Valor Absoluto")
                n1 = int(input("Ingrese el valor: "))
                calest = CalEstandar(0,0)
                print("El valor absoluto es: {}".format(calest.valorAbsoluto(n1)))
                input("presione una tecla para continuar")    
                
            
            if op1 == "8":
                print("Calculadora Ciencitifica --- Circunferencia")
                n1 = int(input("Ingrese el valor a calcular: "))
                calcie = CalCientifica(n1,0)
                print(calcie.circunferencia())
                input("presione una tecla para continuar")
                
                
            if op1 == "9":
                print("Calculadora Cientifica --- Area de un Circulo")
                n1 = float(input("Ingrese el valor a calcular: "))
                calcie = CalCientifica(n1,0)
                print(calcie.areaCirculo())
                input("presione una tecla para continuar")
                
                
            if op1 == "10":
                print("Calculadora Cientifica --- Area de un Cuadrado")
                n1 = int(input("Ingrese el valor del lado 1-2: "))
                n2 = int(input("Ingrese el valor del lado 3-4: "))
                calcie = CalCientifica(n1,n2)
                print(calcie.areaCuadrado())
                input("presione una tecla para continuar")