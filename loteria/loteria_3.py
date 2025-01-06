def valida_entrada():
    while True:
        try:
            numero = int(input("Digite um numero entre 1 e 15: "))
         
        except ValueError:
            return "Erro: Caráctere inválido"

        if 1 <= numero <= 15:
            return numero
        
numero_sorteado = 7

for i in range(3):
    print("Tentativa", i+1)

    numero = valida_entrada()

    if numero == numero_sorteado:
        print("Parabéns!!!")
        break
    elif numero > numero_sorteado:
        print("Tente um número menor!")
    else:
        print("Tente um número maior!")
