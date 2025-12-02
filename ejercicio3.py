from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('producto, disponible, mas_vendido, ID, Nombre, Precio, Ventas, Stock')

+producto(1, 'Laptop', 15000, 120, 5)
+producto(2, 'Mouse', 250, 350, 0)    
+producto(3, 'Teclado', 500, 200, 10)
+producto(4, 'Monitor', 3000, 80, 2)
+producto(5, 'USB 64GB', 150, 400, 25)

disponible(ID, Nombre, Precio, Ventas, Stock) <= producto(ID, Nombre, Precio, Ventas, Stock) & (Stock > 0)

mas_vendido(ID, Nombre, Precio, Ventas, Stock) <= disponible(ID, Nombre, Precio, Ventas, Stock) & (Ventas > 150)

print("\n=== Productos disponibles ===")
for p in disponible(ID, Nombre, Precio, Ventas, Stock):
    print(p)

print("\n=== Productos más vendidos ===")
for p in mas_vendido(ID, Nombre, Precio, Ventas, Stock):
    print(p)
