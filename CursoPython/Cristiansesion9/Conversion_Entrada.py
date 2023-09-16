entrada = input('Ingrese numero: ')

try:
    numero = int(entrada)
    print(numero)
except ValueError:
    print('Error')
else:
    print('La conversion fue exitosa')