#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero,
# obtenga el resultado de la siguiente función:
# 100*V       SI num=1
#100^V        Si num=2
#100/V        Si num=3, para v <>0
#0            cuallquier otro valor de num





class Tarea ():
    def __init__(self):
        pass
    
    def funcion (self):
        num= int(input("Escriba un numero: "))
        V= int(input("Digite un valor: "))
        resp=''
        if num == 1:
            resp=(100*V)
        elif num == 2:
            resp=(100**V)
        elif num == 3 and V != 0:
             resp= (100/V)
        else: 
            resp= (0)
        print("El resultado es de:{} ".format(resp))
            
                                     
eje= Tarea()
eje.funcion()
                
           
        