from twitter import Twitter

def go():
    ## variaveis com keys e tokens para logar na API do twitter
    consumer_key = 'G7dO3c2VrZI0FPQHDsEQB36YR'
    consumer_secret = 'zebriqpeMigNNchlBWxVzlwXQ4xvA42BVbvDszE9vJim11OYGR'
    token_key = '827237475831652356-Fz3ezdFQBWMbrA7cHh5TPd903CgQYXT'
    token_secret = 'WxF8M6Uo6LDtNnrecBoai1mV5rI3AChuL7GfpaYjktiP3'
    tw_connect = Twitter(consumer_key, consumer_secret, token_key, token_secret)


    texto = input('Oque você quer Twittar ? \n')
    j_req = tw_connect.postar(texto)

    ## colocando resultados na tela
    if j_req['created_at']:
            link_post = 'https://twitter.com/'+j_req['user']['screen_name']+'/status/'+j_req['id_str']
            print(' ')
            print('Postou uhuuu, Link:')
            print(link_post)
    else:
            print('2')
