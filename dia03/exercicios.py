#%%

print("Escolha uma água:\n")
print("[1] Mineral\n")
print("[2] Com gás")
agua = input()
quantidade = int(input("Quantas garrafas?"))
if agua == "1":
    preco = 1.50 * quantidade
    print("Preço total:", preco)
elif agua == "2":
    preco = 2.50 * quantidade
    print("Preço total:", preco)

# %%

sorvetes = ["Casquinha", "Cascão", "Cestinha"]
print("[1] Casquinha\n")
print("[2] Cascão\n")
print("[3] Cestinha")
sorvete = input("Escolha um sorvete:")

if sorvete == "1":
    valor = 1.50
elif sorvete == "2":
    valor = 2.50
elif sorvete == "3":
    valor = 4.00
else:
    pass

print("[1] Morango\n")
print("[2] Creme\n")
print("[3] Chocolate")
sabor = input("Escolha seu sabor:")

print("[1] Caramelo\n")
print("[2] Morango\n")
print("[3] Chocolate")
print("[4] Sem Cobertura")
cobertura = input("Escolha sua cobertura:")

if cobertura == "1" or cobertura == "2" or cobertura == "3":
    valor += 1.50
else:
    pass

print("Valor total a ser pago:", valor)
# %%


nome = input("Escreva o nome para o detector de familias averiguar:")
nome = nome.lower()
if "calvo" in nome:
    print("Você é um Calvo")
elif "silva" in nome:
    print("Você é um Silva")
else:
    print("Você é um arromb4do")

# %%

catalogo_loja = ["Laranja", "Cerveja", "Miojo", "Carvão", "Picanha"]

escolha = input("Escolha um item para compra na loja")

if escolha in catalogo_loja:
    print("Você quer comprar um(a)", escolha)
else:
    print("Esse item não está disponível em nosso catálogo, favor tentar novamente")
# %%

frase = input("Digite uma frase:")

letra_a = 0
for letra in frase:
    if letra == "a":
        letra_a += 1

print("A frase possui a letra a ", letra_a, "vezes")
#%%
alturas = []

alturas_adicionadas = 1
while alturas_adicionadas < 4:
    alturas_adicionadas += 1
    altura = int(input("Digite 4 alturas (em centimetros)"))
    alturas.append(altura)

print("A soma de todas as alturas no total é", sum(alturas))

# %%

numeros = [10, 20, 30, 40, 50, 60, 70, 80]

numeros[::-2]
# %%

valores = 0

while True:
    deposito = input("Digite um valor para depositar")
    
    if deposito == "":
        break
    valores += float(deposito)

print(valores)
# %%
print(False * 8)
# %%
