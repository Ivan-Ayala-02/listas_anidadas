def alta_productos(lista:list)->list:
    
    print("\n--- ALTA DE PRODUCTOS ---\n")

    nombre_producto = input("Ingrese el nombre del producto: ")

    cantidad = int(input("Ingrese la cantidad de productos a ingresar: "))
    while cantidad < 0 or cantidad > 100:
        cantidad = int(input("Cantidad invalida, ingrese dentro del rango admitido (0-100): "))

    fila = int(input("Ingrese la fila a ubicar el producto: "))
    if fila > 0:
        fila -= 1
    while fila < 0 or fila > 2:
        fila = int(input("[ERROR] ingrese una fila valida (1-3): "))
        if fila > 0:
            fila -= 1

    columna = int(input("Ingrese la columna a ubicar el producto: "))
    if columna > 0:
        columna -=1
    while columna < 0 or columna > 4:
        columna = int(input("[ERROR] ingrese una columna valida (1-5): "))
        if columna > 0:
            columna -=1
    
    if len(lista[fila][columna]) == 1:
        lista[fila][columna] = [nombre_producto, cantidad, [fila+1, columna+1]]
        print("\nProducto agregado exitosamente!")
    else:
        print("\nEste espacio esta ocupado, intentelo en un lugar disponible.")
    
    return lista



def baja_productos(lista:list)->list:

    print("\n--- BAJA DE PRODUCTOS ---\n")
    fila = int(input("Ingrese la fila a ubicar el producto: "))
    if fila > 0:
        fila -= 1
    while fila < 0 or fila > 2:
        fila = int(input("[ERROR] ingrese una fila valida (1-3): "))
        if fila > 0:
            fila -= 1

    columna = int(input("Ingrese la columna a ubicar el producto: "))
    if columna > 0:
        columna -=1
    while columna < 0 or columna > 4:
        columna = int(input("[ERROR] ingrese una columna valida (1-5): "))
        if columna > 0:
            columna -=1
    
    if len(lista[fila][columna]) != 1:
        lista[fila][columna] = [0]
        print("\nProducto dado de baja exitosamente!")
    else:
        print("\nEste espacio esta vacio anteriormente.")
    
    return lista
    


def modificar_productos(lista:list)->list:

    print("\n--- MODIFICAR CANTIDAD / UBICACION DEL PRODUCTO ---\n")

    fila = int(input("Ingrese la fila a ubicar el producto: "))
    if fila > 0:
        fila -= 1
    while fila < 0 or fila > 2:
        fila = int(input("[ERROR] ingrese una fila valida (1-3): "))
        if fila > 0:
            fila -= 1

    columna = int(input("Ingrese la columna a ubicar el producto: "))
    if columna > 0:
        columna -=1
    while columna < 0 or columna > 4:
        columna = int(input("[ERROR] ingrese una columna valida (1-5): "))
        if columna > 0:
            columna -=1
    
    cambiar_cantidad = input("Desea cambiar la cantidad del producto (s/n)?: ")
    while cambiar_cantidad != "s" and cambiar_cantidad != "n":
        cambiar_cantidad = print("[ERROR] Ingrese una opcion valida (s/n): ")
    
    if cambiar_cantidad == "s":
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        while nueva_cantidad < 0 or nueva_cantidad > 100:
            nueva_cantidad = int(input("Cantidad invalida, ingrese dentro del rango admitido (0-100): "))
        lista[fila][columna][1] = nueva_cantidad   

    cambiar_ubicacion = input("Desea cambiar la ubicacion del producto (s/n)?: ")
    while cambiar_ubicacion != "s" and cambiar_ubicacion != "n":
        cambiar_ubicacion = print("[ERROR] Ingrese una opcion valida (s/n): ")
    
    if cambiar_ubicacion == "s":

        nueva_fila = int(input("Ingrese nueva fila que se desea asignar: "))
        if nueva_fila > 0:
            nueva_fila -= 1
        while nueva_fila < 0 or nueva_fila > 2:
            nueva_fila = int(input("[ERROR] ingrese una fila valida (1-3): "))
            if nueva_fila > 0:
                nueva_fila -= 1

        nueva_columna = int(input("Ingrese la nueva columna que se desea asignar: "))
        if nueva_columna > 0:
            nueva_columna -=1
        while nueva_columna < 0 or nueva_columna > 4:
            nueva_columna = int(input("[ERROR] ingrese una columna valida (1-5): "))
            if nueva_columna > 0:
                nueva_columna -=1
    
        if len(lista[nueva_fila][nueva_columna]) == 1:
            lista[nueva_fila][nueva_columna] = lista[fila][columna]
            lista[fila][columna] = [0]
            print("\nProducto modificado exitosamente!")
        else:
            print("\nEste espacio esta ocupado, intentelo en un lugar disponible.")
        
        return lista



def listar_productos(lista:list):

    print("\n--- LISTA STOCK GENERAL ---\n")

    for i in range(len(lista)):
        print(f"\n--- FILA {i+1} ---\n")
        for j in range(len(lista[i])):
            if len(lista[i][j]) == 1:
                print(f"Columna {j+1}: Vacio")
            else:
                print(f"Columna {j+1}:", lista[i][j])



def listar_prod_por_nombre(lista:list):

    nueva_lista = []

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if len(lista[i][j]) != 1:
                nueva_lista.append(lista[i][j])
    
    for i in range(len(nueva_lista)):
        for j in range(i+1,len(nueva_lista)):
            if nueva_lista[i][0] > nueva_lista[j][0]:
                aux = nueva_lista [i][0]
                nueva_lista[i][0] = nueva_lista [j][0]
                nueva_lista[j][0] = aux
    
    print("\n--- PRODUCTOS DISPONIBLES ORDENADOS POR NOMBRE ---\n")
    for i in range (len(nueva_lista)):
        print()
        for j in range(len(nueva_lista[i])):
            print(nueva_lista[i][j])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def verificar_opcion_elegida(opcion_elegida:int)->int:
    while opcion_elegida < 1 or opcion_elegida > 6:
        opcion_elegida = int(input("[ ERROR ] Ingrese una opcion dentro del rango valido (1-6): "))
    
    return opcion_elegida

def verificar_menu(continuar:str)->str:
    while continuar != "s" and continuar != "n":
        continuar = input("[ ERROR ] Ingrese una opcion valida (s/n): ")

    if continuar == "n":
        print("#----------------------------------------------------------------------------------------#")

    return continuar

