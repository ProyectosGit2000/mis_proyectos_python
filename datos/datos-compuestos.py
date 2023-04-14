# Listas
lista = ["Jordi Chavarry","Soltero",True,1.85,"Jordi Chavarry"]

tupla = ("Jordi Chavarry","Soltero",True,1.85,"Jordi Chavarry")

#print(tupla[1])

#esto es valido(se puede modificar)
lista[1] = "Casado"

#esto no es valido
#tupla[1] = "casado"

#creando un conjunto (set)

# los conjuntos no alamacenan datos duplicados y tambien no accede por indice
conjunto = {"Jordi Chavarry","Soltero",True,1.85,"Jordi Chavarry"}

#print(conjunto[1]) -> esto es incorrecto

#=====================================================================================================================

#creando un diccionario
diccionario = {
    'nombre' : "Jordi Chavarry",
    'edad' : 23,
    'esta_emocionado' : True,
    'altura' : 1.76,
    'dato duplicado' : "Jordi Chavarry"
}

print(diccionario['nombre'])