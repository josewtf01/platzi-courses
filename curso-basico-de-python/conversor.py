def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('¿Cuantos pesos ' + tipo_pesos + ' tienes?: '))
    dolares = pesos / valor_dolar
    dolares = round(dolares,3)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al converso de monedas

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos


Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion == '3':
    conversor('mexicanos', 24)
else:
    print('Ingresa una opcion correcta por favor')


