import Libreria.convercion as LCO
def tmpPreguntar():

    tmp = float (input(""))
    return tmp
pregunta = 'si' 
while pregunta == 'si':
    print("----Conversaciones de Temperatura-----")
    print("1- Celcuis a Fahrenheit\n2- Fahrenheit a Celcius")
    convercion = int(input('Ingrese el numero correspondiente: '))
    if convercion == 1:
        print('Temperatur en celcius: ')
        print('La conversion Celcius a Fahrenhait es: ',
        LCO.cvCelciusFareh(tmpPreguntar()))
    elif convercion == 2:
        print('La temperatura es Fahrenheit: ')
        print('la conversion de Fahrenheit a Celcius es: ',
              LCO.cvFarehCelcius(tmpPreguntar()))
    else:
        print('Numero invalido')

    pregunta = input('Quieres hacer otra conversion: SI o No ').lower()





