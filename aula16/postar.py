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

    ## input para perguntar o que ele quer postar
    texto = input('Oque você quer Twittar ? \n')
    c_texto = urllib.parse.quote(texto, safe='')

    ## requisição na API de postar do twitter
    req = client.request("https://api.twitter.com/1.1/statuses/update.json?status="+ c_texto, method='POST')
    d_req = req[1].decode()
    j_req = json.loads(d_req)

    ## colocando resultados na tela
    if j_req['created_at']:
            link_post = 'https://twitter.com/'+j_req['user']['screen_name']+'/status/'+j_req['id_str']
            print(' ')
            print('Postou uhuuu, Link:')
            print(link_post)
    else:
            print('2')
    