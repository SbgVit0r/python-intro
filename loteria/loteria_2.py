numero_sorteado = 7

for i in range(3):
    print("Tentativa", i+1)
    while True:
        try:
            numero = int(input("Digite um numero entre 1 e 15: "))
            break
        except ValueError:
            print("Caractere inválido")

    if numero == numero_sorteado:
        print("Parabéns!!!")
        break
    elif numero > numero_sorteado:
        print("Tente um número menor!")
    else:
        print("Tente um número maior!")
