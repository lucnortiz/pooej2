import csv
from modulo_sabor import Sabor

class ManejaSabores:
    __sabores= []
    
    def __init__(self):
        self.__sabores= []

    def carga_sabores(self):
        archi_sabores= open("sabores.csv")
        reader= csv.reader(archi_sabores, delimiter=',')
        for fila in reader:
            q= Sabor(int(fila[0]), fila[1], fila[2])
            self.__sabores.append(q)

    def mostrar_sabores(self):
        for i in self.__sabores:
            print (i)
            print("\n")           
    
    def busca_sabor(self,s):
        i= 0
        try:
            while (s != self.__sabores[i].get_nombre() and i < len(self.__sabores)):
                i+=1
            return self.__sabores[i]
        
        except:
            return 0
    
    def busca_indice_sabor(self,s):
        i= 0
        while (s != self.__sabores[i].get_nombre() and i < len(self.__sabores)):
            i+=1
        return i
    
    def devuelve_nombre_sabor(self,indice):
        nom= self.__sabores[indice].get_nombre()
        return nom
    
    
        
        
        
        
        