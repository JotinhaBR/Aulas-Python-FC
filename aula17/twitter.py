import oauth2, json, urllib

class Twitter():

        def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
                self.conexao(consumer_key, consumer_secret, token_key, token_secret)

        def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
                ## verificando e fazendo o login da API do twitter
                self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
                self.token = oauth2.Token(token_key, token_secret)
                self.client = oauth2.Client(self.consumer, self.token)

        def buscar(self, query):
                c_query = urllib.parse.quote(query, safe='')
                self.req = self.client.request("https://api.twitter.com/1.1/search/tweets.json?q="+ c_query)
                self.d_req = self.req[1].decode()
                self.j_req = json.loads(self.d_req)
                return self.j_req

        def postar(self, query):
                c_query = urllib.parse.quote(query, safe='')
                self.req = self.client.request("https://api.twitter.com/1.1/statuses/update.json?status="+ c_query, method='POST')
                self.d_req = self.req[1].decode()
                self.j_req = json.loads(self.d_req)
                return self.j_req