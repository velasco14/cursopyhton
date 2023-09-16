class MenorDeEdadError(Exception):
    pass
try:
    edad = int(input('Digite la edad: '))
    if edad < 18:
        raise MenorDeEdadError('Error: Debes ser mayor de edad.')    
except MenorDeEdadError as e:
        print('Error', e)
else:
    print('Eres mayor de edad!')
finally:
    print('al fin se terminó')