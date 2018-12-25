import oauth2, json, urllib

def go():
    ## variaveis com keys e tokens para logar na API do twitter
    consumer_key = "G7dO3c2VrZI0FPQHDsEQB36YR"
    consumer_secret = "zebriqpeMigNNchlBWxVzlwXQ4xvA42BVbvDszE9vJim11OYGR"
    token_key = "827237475831652356-Fz3ezdFQBWMbrA7cHh5TPd903CgQYXT"
    token_secret = "WxF8M6Uo6LDtNnrecBoai1mV5rI3AChuL7GfpaYjktiP3"

    ## verificando e fazendo o login da API do twitter
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    token = oauth2.Token(token_key, token_secret)
    client = oauth2.Client(consumer, token)

    ## input para perguntar o que ele quer pesquisar
    pesquisar = input('Busca no twitter: ')
    c_pesquisar = urllib.parse.quote(pesquisar, safe='')

    ## requisição na API de pesquisa do twitter
    req = client.request("https://api.twitter.com/1.1/search/tweets.json?q="+ c_pesquisar)
    d_req = req[1].decode()
    j_req = json.loads(d_req)

    ## colocando resultados na tela
    for tweets in j_req['statuses']:
        print(' ')
        print('Tweet do user (', tweets['user']['screen_name'], ')')
        print(tweets['text'])
        print(' ')