import random

palabras = ["python", "programacion", "desafio", "computadora", "aprendizaje"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos_maximos = 6
intentos = 0

while intentos < intentos_maximos:
    letra = input("Ingresa una letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa una sola letra válida.")
        continue
    
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra.")
        continue
    
    letras_adivinadas.append(letra)
    
    palabra_mostrada = ""
    for letra_palabra in palabra_secreta:
        if letra_palabra in letras_adivinadas:
            palabra_mostrada += letra_palabra
        else:
            palabra_mostrada += "_"
    
    print("Palabra:", palabra_mostrada)
    
    if palabra_mostrada == palabra_secreta:
        print("¡Adivinaste la palabra!")
        break
    
    intentos += 1

if intentos == intentos_maximos:
    print("¡Perdiste! La palabra era", palabra_secreta)
