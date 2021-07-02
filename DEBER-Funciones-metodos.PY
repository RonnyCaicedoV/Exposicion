#Leer tres números enteros diferentes entre sí y determinar el número mayor
# de los tres.

class Tarea:
    def __init__(self):
        pass
    
    def numayor (self):
        
        
        N1= int(input("Digite su primer numero: "))
        N2= int(input("Digite su segundo numero: "))
        N3= int(input("Digite su tercer numero: "))
        if N1 > N2 and N1 > N3 :
            Num_mayor= (N1)
        elif N2 > N3:
            Num_mayor= (N2)
        else:
            Num_mayor= (N3)
        print("El numero mayor entre los tres numeros es el : ",Num_mayor)
            
eje= Tarea()
eje.numayor()
        
        
               