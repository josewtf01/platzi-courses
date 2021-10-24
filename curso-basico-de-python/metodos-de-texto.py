# original
nombre = input('Cual es tu nombre?')
print('original - ', nombre)

# todo mayusculas
nombre = nombre.upper()
print('upper - ',nombre)

# la primera letra mayuscula
nombre = nombre.capitalize()
print('capitalized - ', nombre)

# quitar espacios en blanco
nombre = nombre.strip()
print('strip - ', nombre)

# todo minusculas 
nombre = nombre.lower()
print('lower - ', nombre)

# remplazar cadena de texto
nombre = nombre.replace('o','a')
print('replaced - ',nombre)

#longitud de la cadena
print('lenght of the text - ', len(nombre))