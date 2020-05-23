class Sabor:
    __numero= 0
    __nombre= ''
    __descripcion= ''
    
    
    def __init__(self,num,nom,desc):
        self.__numero= num
        self.__nombre= nom
        self.__descripcion= desc
        
    def __str__(self):
        cadenaSabor = 'Numero Sabor: '+ str(self.__numero)
        cadenaSabor += '\nNombre: '+ self.__nombre
        cadenaSabor += '\nDescripcion: ' + self.__descripcion
        return cadenaSabor
    
    def get_numero(self):
        return self.__numero
    
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion