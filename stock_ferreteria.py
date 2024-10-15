from opciones_ferreteria import *

stock = [   
            [["to12", 65],["to16", 86],["to20", 65],["to25", 45]],
            [["to30", 68],["to35", 73],["to40", 85],["to45", 89]],
            [["ta4",  58],["ta5",  48],["ta6",  64],["ta7",  96]],
            [["ta8",  36],["ta10", 72],["ta12", 78],["ta14", 71]]   
        ]

continuar = "s"

while continuar == 's':
    print("\n#----------------------------------------------------------------------------------------#")
    opcion_elegida = int(input("""[ MENU DE OPCIONES FERRETERIA]

Ingrese con un el numero asignado la opcion que se desea ejecutar:
                                
1 - Reponer mercaderia
2 - Vender mercaderia
3 - Listar inventario
4 - Salir
                                   
--> Ingrese una opcion a elegir: """))
    
    opcion_elegida = verificar_opcion_elegida(opcion_elegida)
    print("#----------------------------------------------------------------------------------------#")

    if opcion_elegida == 1:
        stock = reponer_mercaderia(stock)
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)

    if opcion_elegida == 2:
        stock = vender_mercaderia(stock)
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)
    
    if opcion_elegida == 3:
        listar_productos(stock)
        continuar = input("\nDesea continuar (s/n): ")
        continuar = verificar_menu(continuar)
    
    if opcion_elegida == 4:
        continuar = 'n'

print("[ FIN DEL PROGRAMA ]")