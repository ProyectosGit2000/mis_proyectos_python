#repasando lo aprendido xd
a = 10
b = 20
c = a + b

# print(c)

z = 300

letra = type(z)
print(letra)

numero_1 = 30
numero_2 = 30

comparando = numero_1 != numero_2
print(comparando)

pago = 800

if pago > 1500:
    print("trabajaste duro!")
elif pago < 1000:
    print("eres una desgracia")
else:
    print("pobre de mrd")
    
lista = ['jordi',True,"chavarry",1.82]
tupla = ('jordi',True,"chavarry",1.82)
conjunto = {'jordi',True,"chavarry",1.82}
diccionario = {
    'nombre' : "jordi",
    'apellidos' : "chavarry",
    'edad' : 23
}

resultado_1 = True & False
resultado_2 = True & True
resultado_3 = False & True
resultado_4 = False & False

resultado_5 = True | False
resultado_6 = True | True
resultado_7 = False | True
resultado_8 = False | False

resultado_9 = not True
resultado_10 = not False