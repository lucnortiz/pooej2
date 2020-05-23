class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            0:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, sabor, helado,lista_sabor_mas_pedido):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(sabor, helado, lista_sabor_mas_pedido)
        
    def salir(self):
        print('Salir')
        
    def opcion1(self,sabor,helado,lista_sabor_mas_pedido):
        helado.nuevo_pedido_helado(sabor,lista_sabor_mas_pedido)
        
    def opcion2(self,sabor,helado,lista_sabor_mas_pedido):
        helado.sabor_mas_pedido(helado,sabor,lista_sabor_mas_pedido)
        
    def opcion3(self,sabor,helado,lista_sabor_mas_pedid):
        num_sabor= int(input("Ingrese codigo de Sabor a buscar: "))
        helado.calcula_peso_vendido(num_sabor)
    
    def opcion4(self,sabor,helado,lista_sabor_mas_pedido):
        tipo_helado= int(input("Seleccione el tipo de helado (100,150,250,500,1000): "))
        helado.sabores_vendidos(tipo_helado)
        
        