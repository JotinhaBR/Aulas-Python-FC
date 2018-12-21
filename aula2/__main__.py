from datetime import datetime

# variaveis principais
nome = input('Qual seu nome? \n')
data_nascimento = input('Qual sua data de nascimento?  (use o formato DD/MM/YYYY) \n')
data_atual = datetime.now()

# calculadora de idade
nascimento_dia, nascimento_mes, nascimento_ano = map(int, data_nascimento.split('/'))
idade = data_atual.year - nascimento_ano

# pegar tipo das variaveis
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_data_atual = type(data_atual)
tipo_data_nascimento = type(data_nascimento)

# exibindo tudo na tela
print('\n\n\n')
print(str(nome), ', você tem ', str(idade), ' anos')
print(' ')
print(' ')
print('Variaveis:')
print(' ')
print('Nome: ', nome, tipo_nome)
print('Idade: ', idade, tipo_idade)
print('Data atual: ', data_atual, tipo_data_atual)
print('Data de nascimento: ', data_nascimento, tipo_data_nascimento)