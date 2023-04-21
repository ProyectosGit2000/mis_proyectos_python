#metodos de cadenas
texto1 ="hola a todos"
texto2 = "hola jeje"
texto3 = "Tupuedes"

convertir_mayusculas = texto1.upper()

convertir_minusculas = texto1.lower()

primera_mayusculas = texto1.capitalize()

se_ecuentra = texto2.find("o") #si lo encuentra devuelve true y si no devuelve un -1

se_ecuentra2 = texto2.index("o") #si lo encuentra devuelve true y si no devuelve una exepcion

es_numerico = texto3.isnumeric()

es_alpha = texto3.isalpha()

devuelve_coincidencias = texto2.count("e")

cantidad_caracteres = len(texto2)

empieza_con = texto3.startswith("Tu")

termina_con = texto3.endswith("es")

print(devuelve_coincidencias)
