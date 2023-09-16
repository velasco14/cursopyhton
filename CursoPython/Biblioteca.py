
import libreria.Funciones_Bibliotecas as FB

print('Bienvenido al sistema de bibliotecas')

while True:
    print('Digite la opcion a utilizar :\n 1- agregar libros a la biblioteca\n 2- mostrar libros en biblioteca\n 3- buscar libros en biblioteca\n 4- eliminar libro\n 0- salir del sistema')
    opcion = int(input('Ingrese numero de la opcion: '))

    if opcion == 0:
        print('Gracias por usar el sistema')
        break
    elif opcion == 1:
       titulo = input('Ingrese titulo: ')
       autor = input('Ingrese autor: ')
       fecha = input('Ingrese fecha AAAA-MM-DD: ')
       FB.agregar_libros(titulo, autor, fecha)
    elif opcion == 2:
        FB.Mostrar_Libro()
    elif opcion == 3: 
        busqueda = input('Digite el nombre de titulo: ')
        FB.buscar_libros(busqueda)
    elif opcion == 4:
        LibroT = input('Digite el nombre de titulo: ')
        FB.Eliminar_Libro(LibroT)
        print('Libro eliminado con exito\n')
    else:
        print('Opcion invalida')








