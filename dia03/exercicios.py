#%%

preco = 0

aguas = {
    "Mineral" : 1.50,
    "Com gás" : 2.50
}

agua = input("Escolha uma água (Mineral, Com gás):").capitalize()

quantidade = int(input("Quantas garrafas?"))

if agua in aguas:
    preco += aguas[agua]
    preco *= quantidade
    
print("Valor total", preco)

# %%
valor = 0

tipo_sorvete = input("Escolha um sorvete:").capitalize()
sabor = input("Escolha seu sabor[Morango, Creme, Chocolate]:").capitalize()
cobertura = input("Escolha sua cobertura:").capitalize()

sorvetes = {
    "Casquinha" : 1.00, 
    "Cascão" : 2.50, 
    "Cestinha" : 4.00
}

coberturas = {
    "Caramelo" : 1.50,
    "Morango" : 1.50,
    "Chocolate" : 1.50,
    "": 0
}

sabores = ["Morango", "Creme", "Chocolate"]

if tipo_sorvete in sorvetes:
    valor += sorvetes[tipo_sorvete]
else:
    print("Esse tipo não está em nosso catálogo")

if cobertura in coberturas:
    valor += coberturas[cobertura]
else:
    print("Essa cobertura não está em nosso catálogo")


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