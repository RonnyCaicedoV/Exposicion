#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
# utilizando un bucle controlado por el usuario

class Tarea ():
    def __init__(self):
        pass
    def sumaprousua(self):
    
        resp= input("Desea Calcular?: ")
        while resp == "Si" or resp == "si":
            num= int(input("Escriba su numero: "))
            sum= num+num
            prod= num*num
            print("El total de la suma es: ",sum)
            print("El total del  producto es: ", prod)
            resp=input("Desea seguir: ")
        print("Gracias, tenga un buen dia ")
       
        
eje= Tarea()
eje.sumaprousua()
            
        