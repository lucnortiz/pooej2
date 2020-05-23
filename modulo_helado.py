class Helado:
    __gramos= 0
    __sabores= []
    
    def __init__(self,gr,sbr):
        self.__gramos= gr
        self.__sabores= sbr
            
    def __str__(self):
        cadenaHelado = 'Gramos: '+ str(self.__gramos)
        for i in range(len(self.__sabores)):
            cadenaHelado += '\nGusto: '+ self.__sabores[i].get_nombre()
        return cadenaHelado
    
    def get_gramos(self):
        return self.__gramos
    
    def get_cant_sabores(self):
        return len(self.__sabores)
    
    def cargar_lista_codigos(self):
        lista_aux= []
        for i in range(len(self.__sabores)):
            lista_aux.append(self.__sabores[i].get_numero())
        return lista_aux
    
    def cargar_lista_nombres(self):
        lista_aux= []
        for i in range(len(self.__sabores)):
            lista_aux.append(self.__sabores[i].get_nombre())
        return lista_aux
        