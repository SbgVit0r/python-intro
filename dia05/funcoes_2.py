#%%
def soma(op, *num):
    total = 0
    if op == "soma":
        sum(num)
    elif op == "multi":
        total=1
        for i in num:
            total *= i
    for i in num:
        total += i
    return total

soma("multi",1,2,3,4,5,6,7,8,9,10)
# %%

pessoas = ['Fulano', 'Ciclano', 31, ['souivuj', 'wsdogiu', 'duiafh']]
pessoa, pessoinha, *_ = pessoas
print(pessoa)
print(pessoinha)
# %%
x = 10, 20
type(x)
# %%
