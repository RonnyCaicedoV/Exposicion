#Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones 
# aplicando el factorial de un número.


class Tarea:
    def __init__(self):
        pass
    
    def factorial(self):
        n= int(input("Ingrese su cantidad de numeros: "))
        for i in range(n):
            numero= int(input("Ingrese un numero: "))
            fact=1
            for num in range(numero,0,-1):
                fact=fact*num 
            
            print("Factorial del numero:{} es:{}".format(numero,fact))
            
eje= Tarea()
eje.factorial()
            
        
    