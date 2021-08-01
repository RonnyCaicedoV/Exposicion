from menuss import Menu
from basicoo import Basico, Intermedio
import os        
opcion = ""  
while opcion != "5": 
    men= Menu("Menu Principal",["1) Calculadora","2) Numeros","3) Listas","4) Operaciones de cadenas","5) Salir"])
    opcion = men.menu()
    os.system ("cls")
 
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
                    
print("Muchas gracias por su visita, vuelva cuando quiera")
            
        
        
        
    