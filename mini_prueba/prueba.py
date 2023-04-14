#variables
a = 8
b = 6
c = a + b

nombre = "Arturo"
bienvenida_evento = "Hola "+ nombre + " ,como te va!"

nombre2 = "Rosa"
# del nombre2
welcome = f"Hello {nombre2} como te va muchacha" 

print("Hello" not in welcome)
print("Hello" in welcome)

lista = ["Nombre",True,"Chavez",28,1.85]
tipo_de_dato = type(lista)
print(tipo_de_dato)

tupla = ("Nombre",True,"Chavez",28,1.85)
#tupla[1] = False #esto es incorrecto porque no se puede modificar
tipo_de_dato2 = type(tupla)
print( tupla )
 
#en un conjunto no se puede acceder por el numero de indice y tampoco se pueden repetir los datos
conjunto  = {"Nombre",True,"Chavez",28,1.85,"Nombre"}
print(conjunto)

diccionario = {
    'nombre' : "Juansito",
    'edad' : 23,
    'altura' : 1.88
}

print(diccionario["nombre"])