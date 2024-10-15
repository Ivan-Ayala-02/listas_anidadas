def reponer_mercaderia(lista:list)->list:

    print("\n--- REPONER STOCK MERCADERIA ---\n")
    fila = int(input("Ingrese la fila a ubicar el producto: "))
    if fila > 0:
        fila -= 1
    while fila < 0 or fila > 3:
        fila = int(input("[ERROR] ingrese una fila valida (1-4): "))
        if fila > 0:
            fila -= 1

    columna = int(input("Ingrese la columna a ubicar el producto: "))
    if columna > 0:
        columna -=1
    while columna < 0 or columna > 3:
        columna = int(input("[ERROR] ingrese una columna valida (1-4): "))
        if columna > 0:
            columna -=1
    
    cambiar_cantidad = input("Desea cambiar reponer el stock del producto (s/n)?: ")
    while cambiar_cantidad != "s" and cambiar_cantidad != "n":
        cambiar_cantidad = print("[ERROR] Ingrese una opcion valida (s/n): ")
    
    if cambiar_cantidad == "s":
        nueva_cantidad = int(input("Ingrese la cantidad a ingresar (Esta sera sumada a la cantidad ya existente si es que hay): "))
        while nueva_cantidad < 0:
            nueva_cantidad = int(input("Cantidad invalida, ingrese un valor positivo (Mayor a cero): "))
        lista[fila][columna][1] += nueva_cantidad  

    print("\nProducto ingresado de forma exitosa!")
    return lista



def vender_mercaderia(lista:list)->list:

    print("\n--- BAJA DE PRODUCTOS ---\n")
    fila = int(input("Ingrese la fila a ubicar el producto: "))
    if fila > 0:
        fila -= 1
    while fila < 0 or fila > 3:
        fila = int(input("[ERROR] ingrese una fila valida (1-4): "))
        if fila > 0:
            fila -= 1

    columna = int(input("Ingrese la columna a ubicar el producto: "))
    if columna > 0:
        columna -=1
    while columna < 0 or columna > 3:
        columna = int(input("[ERROR] ingrese una columna valida (1-4): "))
        if columna > 0:
            columna -=1
    
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
    if lista[fila][columna][1] == 0:
        print("No hay stock disponible para la venta, reponer mercaderia primero.")
        return lista
    while cantidad_vendida < 0 or cantidad_vendida > lista[fila][columna][1]:
        cantidad_vendida = int(input(f"Cantidad invalida, ingrese un valor dentro del rango permitodo (0-{lista[fila][columna][1]}): "))
    lista[fila][columna][1] -= cantidad_vendida  
    
    return lista



def listar_productos(lista:list):

    print("\n--- LISTA INVENTARIO GENERAL ---\n")

    for i in range(len(lista)):
        print(f"\n--- FILA {i+1} ---\n")
        for j in range(len(lista[i])):
                print(f"Columna {j+1}:", lista[i][j])



#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def verificar_opcion_elegida(opcion_elegida:int)->int:
    while opcion_elegida < 1 or opcion_elegida > 4:
        opcion_elegida = int(input("[ ERROR ] Ingrese una opcion dentro del rango valido (1-4): "))
    
    return opcion_elegida

def verificar_menu(continuar:str)->str:
    while continuar != "s" and continuar != "n":
        continuar = input("[ ERROR ] Ingrese una opcion valida (s/n): ")

    if continuar == "n":
        print("#----------------------------------------------------------------------------------------#")

    return continuar
