from opciones_almacen import *

stock = [   
            [[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0]],
        ]


stock [0][1] = ["botellas", 3, [1, 2]]
stock [0][3] = ["frascos", 8, [1, 4]]
stock [1][2] = ["fideos", 4, [2, 3]]
stock [2][3] = ["leches", 6, [3, 4]]

#print(len(stock[0][3]))

alta = False
continuar = 's'

while continuar == 's':
    print("\n#----------------------------------------------------------------------------------------#")
    opcion_elegida = int(input("""[ MENU DE OPCIONES ALMACEN]

Ingrese con un el numero asignado la opcion que se desea ejecutar:
                                
1 - Alta de productos (producto nuevo)
2 - Baja de productos (producto existente)
3 - Modificar productos (cantidad, ubicación)
4 - Listar productos
5 - Lista de productos ordenado por nombre
6 - Salir
                                   
--> Ingrese una opcion a elegir: """))
    
    opcion_elegida = verificar_opcion_elegida(opcion_elegida)
    print("#----------------------------------------------------------------------------------------#")

    if opcion_elegida == 1:
        stock = alta_productos(stock)
        alta = True
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)

    if opcion_elegida == 2:
        if alta == True:
            stock = baja_productos(stock)
        else:
            print("[ERROR] Es necesario dar un producto de alta primero.")
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)

    if opcion_elegida == 3:
        if alta == True:
            stock = modificar_productos(stock)
        else:
            print("[ERROR] Es necesario dar un producto de alta primero.")
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)
    
    if opcion_elegida == 4:
        listar_productos(stock)
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)

    if opcion_elegida == 5:
        listar_prod_por_nombre(stock)
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)
    
    if opcion_elegida == 6:
        continuar = 'n'

print("[ FIN DEL PROGRAMA ]")
