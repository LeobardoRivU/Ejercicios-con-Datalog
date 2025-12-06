from pyDatalog import pyDatalog 
pyDatalog.clear() 

pyDatalog.create_terms('producto, mas_vendido, bajo_stock') 
pyDatalog.create_terms('ID, Nombre, Precio, Ventas, Stock') 

+producto( 1, "Cemento Tolteca 50kg",          195,  320, 150)
+producto( 2, "Varilla 3/8 corrugada",        128,  580,  80)
+producto( 3, "Block de cemento 12x20x40",     18, 1200, 300)
+producto( 4, "Arena fina bulto 40kg",        85,  420,  45)
+producto( 5, "Grava bulto 40kg",              92,  380,  20)
+producto( 6, "6", "Alambre recocido #16",   890,  150,   8)
+producto( 7, "Lámina galv. calibre 26",      680,   95,  12)
+producto( 8, "Pintura Vinílica 19L blanca",  1250,   78,   0) 
+producto( 9, "Cable THW calibre 12",         42,  890, 200)
+producto(10, "Tubo PVC 1/2\" (6m)",           68,  650,   0)
+producto(11, "Clavo 2.5\" bolsa 1kg",         48, 1100, 120)
+producto(12, "Yeso 40kg",                    178,  210,  35)
mas_vendido(ID, Nombre, Ventas) <= ( producto(ID, Nombre, Precio, Ventas, Stock) & (Ventas > 50) ) 
bajo_stock(ID, Nombre, Stock) <= ( producto(ID, Nombre, Precio, Ventas, Stock) & (Stock < 10) ) 
def obtener_lista_filtrada(): 
    lista = producto(ID, Nombre, Precio, Ventas, Stock).data 
    return [p for p in lista if p[4] >= 1]

def imprimir_tabla(): 
    lista = obtener_lista_filtrada() 
    print("\nLISTA DE PRODUCTOS (stock >= 1)") 
    print("ID | Nombre | Precio | Ventas | Stock") 
    print("-------------------------------------------------") 
    for p in lista: 
        print(f"{p[0]:2} | {p[1]:18} | {p[2]:6} | {p[3]:6} | {p[4]:5}")

def imprimir_mas_vendidos(): 
    lista = obtener_lista_filtrada() 
    filtrados = [p for p in lista if p[3] > 50] 
    if not filtrados: 
        print("\nNo hay productos muy vendidos.") 
        return 
    
    orden = sorted(filtrados, key=lambda x: x[3], reverse=True) 

    print("\nPRODUCTOS MÁS VENDIDOS (>50)") 
    print("ID | Nombre | Ventas") 
    print("-----------------------------------")
    for p in orden: print(f"{p[0]:2} | {p[1]:18} | {p[3]}")

def producto_stock_mayor(): 
    lista = obtener_lista_filtrada() 
    return max(lista, key=lambda x: x[4]) if lista else None 
    
def producto_stock_menor(): 
    lista = obtener_lista_filtrada() 
    return min(lista, key=lambda x: x[4]) if lista else None 
    
def producto_mas_vendido_simple(): 
    lista = obtener_lista_filtrada() 
    return max(lista, key=lambda x: x[3]) if lista else None 

def producto_menos_vendido_simple(): 
    lista = obtener_lista_filtrada() 
    return min(lista, key=lambda x: x[3]) if lista else None 

def buscar(nombre): 
    lista = obtener_lista_filtrada() 
    for p in lista: 
        if p[1].lower() == nombre.lower(): 
            return p 
    return None

def menu(): 
    while True: 
        print("\n===============================") 
        print("           INVENTARIO          ") 
        print("===============================") 
        print("1. Ver productos") 
        print("2. Ver productos más vendidos") 
        print("3. Ver productos con bajo stock") 
        print("4. Stock más alto") 
        print("5. Stock más bajo") 
        print("6. Producto más vendido") 
        print("7. Producto menos vendido") 
        print("8. Buscar producto por nombre") 
        print("9. Salir") 
        print("===============================") 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            imprimir_tabla()
        elif opcion == "2":
            imprimir_mas_vendidos() 
        elif opcion == "3":
            print("\nPRODUCTOS CON BAJO STOCK")
            print(bajo_stock(ID, Nombre, Stock))
        elif opcion == "4":
            print("\nPRODUCTO CON STOCK MÁS ALTO: ",producto_stock_mayor()) 
        elif opcion == "5": 
            print("\nSTOCK MÁS BAJO:", producto_stock_menor()) 
        elif opcion == "6": 
            print("\nPRODUCTO MÁS VENDIDO:", producto_mas_vendido_simple()) 
        elif opcion == "7": 
            print("\nPRODUCTO MENOS VENDIDO:", producto_menos_vendido_simple()) 
        elif opcion == "8": 
            nombre = input("Nombre del producto: ") 
            r = buscar(nombre) 
            print("\nResultado:", r if r else "No encontrado") 
        elif opcion == "9": 
            print("\nSaliendo…") 
            break 
        else: print("Opción no válida") 
        
menu()    