#En una tienda se ofrece un descuento del 15% sobre el total de la compra y un 
#cliente desea saber cuánto deberá pagar finalmente por su compra.
class ejem1:
    def __init__(self):
        pass
    
    def total_pagar(self):
        Compra_total= int(input("Ingrese su total de la compra: "))
        descto= Compra_total*0.15
        totalapagar= Compra_total-descto
        print("Su valor de compra es de: {} Su descuento es de: {} Y su valor total a pagar es de : {}".format(Compra_total,descto,totalapagar))
        
Ej1= ejem1()
Ej1.total_pagar()