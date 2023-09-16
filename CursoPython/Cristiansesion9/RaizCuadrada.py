import math
class RaizNegativaError(Exception):
    pass
    class ValorNoNumericoError(Exception):
        pass
def Calcular_Raiz (numero):
     if numero < 0:
             raise RaizNegativaError('Nose pueden calcular raices de numeros negativos')
     return math.sqrt(numero)
try:
    numero = float(input('Ingresa numero: '))
    resultado = Calcular_Raiz(numero)
except RaizNegativaError as er:
            print('error', er)
except ValueError:
     print('error: ingree un valor numerico valido')
else:
     print(f'La raiz cuadrada de {numero} es: {resultado : .2f}')
            


        

                            
    
