def definicion_segura(Numerador, denominador):
    try:
           resultado = Numerador / denominador
           return resultado
    except ZeroDivisionError:
          print('no se puede dividir entre 0')
    except ValueError:
          print('ha ocrruido un problema')
    except:
        print('Ha ocurrido un problema')
try:
      x = int(input('Digite numerador: '))
      y = int(input('Digite denominador: '))
      definicion_segura(x,y)
except ValueError:
      print('Debe ingresar numeros enteros')
      


