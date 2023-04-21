cadena_1 = "Bienveidos papus"
cadena_2 = "MasterProsa"

#convirtiendo a mayusculas
mayusc = cadena_1.upper()

#convirtiendo a minusculas
minusc = cadena_2.lower()

#primera letra mayuscula
primera_letra_mayusc = cadena_1.capitalize()

#buscar una cadena en otra cadena, si no hay devuelve -1
busqueda_find = cadena_2.find("u")

#buscar una cadena en otra cadena, si no la encuentra nos arroja una exepcion
hacer_index = cadena_2.index("a")

#texto numerico
es_numerico = cadena_1.isnumeric()

#texto alphanumerico
es_alphanumerico = cadena_2.isalpha()

#buscar una cadena en otra cadena, y nos devuelve el numero de coincidencias q encuentre
contar_coincidencias = cadena_2.count("a")

#buscar una cadena en otra cadena, y nos devuelve el numero de caracteres q encuentre
nro_caracteres = len(cadena_2)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena_2.startswith("Pro")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena_2.endswith("Prosa")



print(nro_caracteres)