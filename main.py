from modulo_maneja_sabor import ManejaSabores
from modulo_maneja_helados import ManejaHelados
from menu import Menu

if __name__=='__main__':
    sabor= ManejaSabores()
    helado= ManejaHelados()
    lista_sabor_mas_pedido= [0,0,0,0,0,0]
   
    sabor.carga_sabores()
    
    '''
    ## 1 PEDIDO DE HELADOS ##
    
    helado.nuevo_pedido_helado(sabor,lista_sabor_mas_pedido)


    ## 2 MÁS PEDIDOS ##
    
    helado.sabor_mas_pedido(helado,sabor,lista_sabor_mas_pedido)
    
    ## 3 PESO VENDIDO POR CODIGO DE SABOR ##
    
    num_sabor= int(input("Ingrese codigo de Sabor a buscar: "))
    helado.calcula_peso_vendido(num_sabor)
    
    ## 4 SABORES VENDIDOS POR TIPO DE HELADO ##
    
    tipo_helado= int(input("Seleccione el tipo de helado(100,150,250,500,1000): "))
    helado.sabores_vendidos(tipo_helado)
    '''
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Nuevo pedido de Helado\n2. Listar los 5 sabores más pedidos")
        print("3. Gramos vendidos por Sabor\n4. Sabores vendidos por tipo de helado\n0. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op,sabor,helado,lista_sabor_mas_pedido)
        salir = op == 0
    print(salir)