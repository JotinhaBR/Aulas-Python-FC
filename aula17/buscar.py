from twitter import Twitter

def go():
    ## variaveis com keys e tokens para logar na API do twitter
    consumer_key = "G7dO3c2VrZI0FPQHDsEQB36YR"
    consumer_secret = "zebriqpeMigNNchlBWxVzlwXQ4xvA42BVbvDszE9vJim11OYGR"
    token_key = "827237475831652356-Fz3ezdFQBWMbrA7cHh5TPd903CgQYXT"
    token_secret = "WxF8M6Uo6LDtNnrecBoai1mV5rI3AChuL7GfpaYjktiP3"
    tw_connect = Twitter(consumer_key, consumer_secret, token_key, token_secret)

    ## input para perguntar o que ele quer pesquisar
    pesquisar = input('Busca no twitter: ')
    j_req = tw_connect.buscar(pesquisar)

    ## colocando resultados na tela
    for tweets in j_req['statuses']:
        print(' ')
        print('Tweet do user (', tweets['user']['screen_name'], ')')
        print(tweets['text'])
        print(' ')