from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

# Hechos
+padre('juan', 'maria')
+padre('juan', 'pedro')
+padre('pedro', 'ana')
+padre('carlos', 'juan')   
+padre('carlos', 'sofia')    
+padre('sofia', 'luis')      
+padre('pedro', 'julia')     
+padre('juan', 'luis')  

# Regla:
# abuelo(X,Z) si X es padre de Y y Y es padre de Z
abuelo(X, Z) <= padre(X, Y) & padre(Y, Z)


print("Abuelos:")
for a, n in abuelo(X, Y):
    print(f"{a} es abuelo de {n}")
