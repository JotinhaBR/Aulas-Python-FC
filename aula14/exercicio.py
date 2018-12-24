import requests, json

res = requests.get('https://economia.awesomeapi.com.br/all')
j_res = json.loads(res.text)

m_comparada = j_res['USD']['codein']
print('Mostro se liga no valor das moedas:')
print('')
for moeda in j_res:
    print(moeda,' Está valendo ',j_res[moeda]['ask'], j_res[moeda]['codein'])

print('')
print('Info by: https://economia.awesomeapi.com.br/all')