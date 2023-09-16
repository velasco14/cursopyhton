def primo(numero):
       if numero <= 1:
        return False
       for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        return True
numero_limite = int(input("Ingrese un número: "))
print("Números primos menores que", numero_limite, ":")
for num in range(2, numero_limite):
    if primo(num):
        print(num)




