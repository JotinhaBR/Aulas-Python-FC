import requests, json

cidade = input("Mostrão fala qual é a cidade: ")

tokenAPI = '2a34b7f639746559f66b71398bba5f38'

try:
    ## requisição para descobrir id da cidade
    res = requests.get('http://apiadvisor.climatempo.com.br/api/v1/locale/city?name='+cidade+'&token='+tokenAPI)
    id_cidade = json.loads(res.text)
    id_cidade = str(id_cidade[0]['id'])
    
    ## requisição para descobrir o clima com base no ida da cidade
    res = requests.get('http://apiadvisor.climatempo.com.br/api/v1/weather/locale/'+id_cidade+'/current?token='+tokenAPI)
    j_res = json.loads(res.text)

    print('\n ')
    print("Mostrão se liga na previsão climatica da cidade "+j_res['name'])
    print(' ')
    print('Em ', j_res['name'], ' está fazendo ', j_res['data']['temperature'], '°C', )
    print('E as condições climaticas são de ', j_res['data']['condition'])
    print('Ultima atualização: ', j_res['data']['date'])
except:
    print('\n ')
    print('Mostrão digita o nome da cidade certa !!!')