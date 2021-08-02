class Cadena:
    def __init__(self, cadena):
        self.cadena=cadena
        
    def  recorrerCadena(self):
        cont = 0
        for i, caracter in enumerate(self.cadena):
            cont += 1
            print("Caracter {}: {} ".format(cont,caracter))

    def  buscarCaracter(self,buscado):
        x = self.cadena.find(buscado)
        if x != -1:
            return x
        else:
            return "error"
        
    def  listaPosiciones(self,caracter):
        res = []
        for pos1 in range(len(self.cadena)):
            for pos2 in range(len(caracter)):
                if self.cadena[pos1] == caracter[pos2]:
                    res.append(pos1)
        return res

    def listaPalabras(self):
        lista = self.cadena.split()
        return lista


    def cadenaLista(self,lista):
        return " ".join(map(str,lista))
    

    def insertarDato(self,buscado,posicion):
        lista = self.cadena.split()
        lista.insert(posicion,buscado)
        lista1 = Cad.cadenaLista(lista)
        return lista1


    def eliminarOcurrencias(self,buscado):
        if buscado == str(buscado):
            elim = self.cadena.split(buscado)
            modificado = Cad.cadenaLista(elim)
            return modificado
        if buscado == int(buscado):
            x = self.cadena[:buscado] + self.cadena[buscado+1:]
            modificado = Cad.cadenaLista(x)
            return modificado


    def retornaValor(self, posicion):

        lista = list(self.cadena)
        aux = lista[posicion]
        x = self.cadena.replace(aux,"")
        return aux,x


    def concatenarCadena(self,dato):
        self.cadena = self.cadena + " "
        return self.cadena + dato

cadena = ""
Cad = Cadena(cadena)