def Convert_2_int (cadena):
    try:
        entero = int (cadena)
        return entero
    except ValueError:
        print("Error: La cadena no es valida")

cad = '12345678' 
intCad = Convert_2_int(cad)
type(intCad)