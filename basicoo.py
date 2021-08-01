

from ast import Num


class Basico:
     
    def  numerosN(n1):
        n1= int(input("Escriba numero de n: "))
        print("Los numeros de 1 a n son: ")
        for x in range(1,n1+1):
            print(x, end=" ")
    def  numerosNsuma(n):
        n= int(input("Escriba el valor de n: "))
        suma= n * (n + 1)/2
        print(suma)
    
    def multiplo(numero,multip):
        numero= int(input("Digite el primer numero: "))
        multip= int(input("Digite el segundo numero: "))
        if numero % multip == 0:
            print("El numero {} si es multiplo de {} ".format(numero,multip))
        else: print("El numero {} no es multiplo de {} ".format(numero,multip))
        
    def DivisoresNumero(numero):
        conta_divisores= 0
        numero= int(input("Digite su numero: "))
        for i in range(1, numero + 1):
            if numero % i == 0:
                conta_divisores +=1
        return conta_divisores
    
    def primo(numero):
        numero = int(input("Digite el numero: "))
        esPrimo = True
        for c in range (2,numero):
            if numero%c==0:
                esPrimo= False
                break
        if esPrimo:
            print("El numero {} es primo".format(numero))
        else: print("El numero {} no es primo".format(numero))
        
    def perfecto(numero):
        suma = 0
        numero = int(input("Digite un numero: "))
        print("El numero es perfecto?: ")
        for d in range(1, numero):
            if numero % d == 0:
                suma += d
        return suma == numero
        
    
class Intermedio (Basico):
    def  numerosN(n):
        for x in range(1,n+1):
            return x
        
            
    
    
    def factorial(numero):
        numero = int(input("Digite un numero: "))
        factorial=1
        if numero != 0:
            for a in range(1,numero+1):
                factorial= factorial*a
        print("Factorial: ", factorial)
        
        
    def fibonacci(n):
        limite = int(input("Escriba su limite: "))
        a = 1
        b = 0
        for s in range(0, limite):
            b = b+a
            a = b-a
            print(a, end=" ") 
            
            
    def primosGemelos(num1,num2):
        comprobar= True
        while comprobar:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            a=0
            if num1 > 0 and num2 > 0 and num1 != num2:
                comprobar = False
                if num1 > num2:
                     num1 ^= num2
                     num2 ^= num1
                     num1 ^= num2
                for i in range (num1, num2+1):
                    creciente = 2
                    esPrimo = True
                    while esPrimo and creciente < i:
                        if i % creciente == 0:
                            esPrimo = False
                        else:
                            creciente +=1
                    if esPrimo and not a:
                        a = i
                    elif esPrimo and a:
                        b = i
                        if b-a ==2:
                            print(a, "y",b, "Son primos gemelos")
                        a = i
            else:
                if num1 == num2:
                    print ("Los numeros son iguales. Intente de nuevo..")
                else:
                    print ("Los numeros no son correctos, intente de nuevo...")
         
                
    def amigos (num1, num2):
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        vec_1=[]
        vec_2= []
        sum_1= 0
        sum_2= 0
        for i in range (1,num1):
            if num1 % i == 0:
                vec_1.append(i)
                
        for i in range(1,num2):
            if num2 % i == 0:
                vec_2.append(i)
        
        for k in vec_1:
            sum_1=  sum_1 + k
        for k in vec_2:
            sum_2= sum_2 + k
            
        if sum_1 == num2 and sum_2 == sum_1:
            print("Los numeros son amigos")
        else:
            print("Los numeros no son amigos")
            
                
                    
               
""" Nnum = Basico()
print(Nnum.numerosN()) """ 

""" sumN= Basico()
sumN.numerosNsuma() """

""" multi= Basico()
multi.multiplo() """
     
""" divi = Basico()
print(divi.DivisoresNumero()) """

""" prim= Basico()
prim.primo()"""

""" Fact = Intermedio()
Fact.factorial() """

""" perfec= Basico()
perfec.perfecto() """

""" fibo= Intermedio()
fibo.fibonacci() """

""" priGem= Intermedio()
priGem.primosGemelos(()) """



""" ami= Intermedio()
ami.amigos(()) """