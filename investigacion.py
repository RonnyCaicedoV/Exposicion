from menuss import Menu
from basicoo import Basico 
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
                n= int(input("Escriba el valor de n: "))
                print("Los numeros de 1 a n son: ")
                Nnum = Basico()
                print(Nnum.numerosN(), end=" ")
                input("Pulse cualquier tecla si desea continuar...")
                
            if opci1 == "2":
                os.system ("cls")
                print("Suma de 1 a n")
                n= int(input("Escriba el valor de n: "))
                suma= n * (n + 1)/2
                print(suma)
            
            if opci1 == "3":
                os.system ("cls")
                print("Multiplo de numero")
                a = int(input("Digite el primer numero: "))
                b = int(input("Digite el segundo numero: "))
                if a % b == 0:
                    print("El numero {} si es multiplo de {} ".format(a,b))
                else: print("El numero {} no es multiplo de {} ".format(a,b))
                    
print("Muchas gracias por su visita, vuelva cuando quiera")
            
        
        
        
    