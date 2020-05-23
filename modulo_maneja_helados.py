from modulo_helado import Helado


class ManejaHelados:
    __helados= []
    
    def __init__(self):
        self.__helados=[]
        
    def nuevo_pedido_helado(self,sabor,mas_pedido):
        lista_sabores= []
        print (">>> Nuevo Pedido de Helado <<<\n")
        print ("1- 100grs\n2- 150grs\n3- 250grs\n4- 500grs\n5- 1000 grs")
        op= int(input("Ingrese opción: "))
        g= self.devuelve_gramos(op)
        if (g == 0):
            print ("Opcion incorrecta.")
        else:      
            cant_sabores = int(input("Ingrese cantidad de Sabores: "))
            if (cant_sabores <= 4 and cant_sabores >= 1):
                i= 0
                while (i < cant_sabores):
                    s= input(f"Ingrese nombre de sabor {i+1}: ")
                    o= sabor.busca_sabor(s)
                    
                    if (o == 0):
                        print ("Sabor Incorrecto")
                    else:
                        lista_sabores.append(o)
                        ind= sabor.busca_indice_sabor(s)
                        mas_pedido[ind]+=1
                        i+=1
    
    
                self.__helados.append(Helado(g,lista_sabores))
                print ("Pedido de Helado Cargado\n---------\n")
            else:
                print ("Puede ser de 1 a 4 sabores.")

    def devuelve_gramos(self,op):
        if (op == 1):
            g= 100
        elif (op == 2):
            g= 150
        elif (op == 3):
            g= 250 
        elif (op == 4):
            g= 500 
        elif (op == 5):
            g= 1000
        else:
            g= 0
            
        return g

    def mostrar_helados(self):
        for i in self.__helados:
            print (i)
            print("\n")
            
    def sabor_mas_pedido(self,helado,sabor,lista):
        lista_aux = lista
        indMax= 0
        for j in range(5):
            max= 0
            for i in range(6):   
                if (lista_aux[i] > max):
                    max= lista_aux[i]
                    indMax= i
            
            if (max != 0):
                nom= sabor.devuelve_nombre_sabor(indMax)
                print (f"{nom} fue pedido {max} veces")
                lista_aux[indMax] = -1
    
    def calcula_peso_vendido(self,codigo_sabor):
        suma= 0
        for i in range(len(self.__helados)):
            lista_codigos= []
            lista_codigos= self.__helados[i].cargar_lista_codigos()
            if codigo_sabor in lista_codigos:
                suma += (int(self.__helados[i].get_gramos()) / int(self.__helados[i].get_cant_sabores()))
        
        print (f"Peso vendido de codigo {codigo_sabor}: {suma}")           

    def sabores_vendidos(self,tipo_helado):
        lista_sabores= []
        lista_aux= []
        for i in range(len(self.__helados)):
            if (tipo_helado == self.__helados[i].get_gramos()):
                lista_aux = self.__helados[i].cargar_lista_nombres()
                for i in range(len(lista_aux)):
                    if lista_aux[i] not in lista_sabores:
                        lista_sabores.append(lista_aux[i])
                
        print (f">>> LISTA DE SABORES EN HELADOS DE {tipo_helado} GRAMOS <<<\n\n")
        for j in range(len(lista_sabores)):
            print (f"{lista_sabores[j]}")
        
        
        
        
        