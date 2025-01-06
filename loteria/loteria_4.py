def checar_entrada():
    """
    Solicita ao usuário que digite um número e tenta convertê-lo para um inteiro.
    Caso o usuário insira um valor não numérico, retorna uma mensagem de erro.
    
    Returns:
        int: O número digitado pelo usuário, se for um número válido.
        str: Mensagem de erro caso o valor não seja um número inteiro.
    """
    try:
        return int(input("Digite um numero entre 1 e 15: "))
    except ValueError:
        return "Erro: Caráctere inválido"

def checar_intervalo(numero):
    """
    Verifica se um número está dentro do intervalo válido (entre 1 e 15).

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número estiver no intervalo de 1 a 15, inclusive.
              False caso contrário.
    """
    return 1 <= numero <= 15

def valida_entrada():
    """
    Função que valida a entrada do usuário, garantindo que o número seja inteiro,
    dentro do intervalo permitido e que não ocorra erro de conversão.

    Returns:
        int: O número válido escolhido pelo usuário, dentro do intervalo de 1 a 15.
    """
    while True:
        numero = checar_entrada()
        if type(numero) != int:
            print(numero)
            continue

        if checar_intervalo(numero):
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
