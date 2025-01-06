#%%
import requests

url = 'https://api.opendota.com/api/heroes'

resposta = requests.get(url)
# %%
resposta.status_code
# %%
dados = resposta.json()
# %%
dados[2]['name']
# %%
for i in dados:
    print(i['name'])
# %%
import pandas as pd
df = pd.DataFrame(dados)
df.to_csv("heroes_dota.csv", sep=';')
# %%
