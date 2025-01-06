#%%
arquivo = open("arquivo.txt", 'a') # w
arquivo.write("bomdia\n")
arquivo.close()
# %%
arquivo = open("arquivo.txt", 'r')
letras = arquivo.read()
arquivo.close()
print(letras)
# %%
arquivo = open("arquivo.txt", 'r')
linhas = arquivo.readlines()
arquivo.close
print(linhas)
# %%

with open("arquivo.txt", 'r') as file:
    conteudo = file.read()

print(conteudo)
# %%
