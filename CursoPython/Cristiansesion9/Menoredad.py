class MenorDeEdadError(Exception):
    def __init__(Error, edad):
        Error.edad = edad
        Error.mensaje = f"Error! La edad ingresada es menor de 18 años."
def verificar_edad(edad):
    if edad < 18:
        raise MenorDeEdadError(edad)
    else:
        print("Acceso concedido. Puedes continuar.")
try:
    edad = int(input("Ingrese su edad: "))
    verificar_edad(edad)
except MenorDeEdadError as e:
    print(e.mensaje)
except ValueError:
    print("Error: Ingrese un valor numérico válido para la edad.")