from mostro import Mostro
import time

print(' ')
print('Ta saindo da jaula o mostro ')
time.sleep(2.5)

mostro = Mostro("Bambam", 1.7, 2)

print('Biirrlll mostro saiu da jaula')
time.sleep(0.5)
print('Nome: ', mostro.nome)
print('Altura: ', mostro.altura)
print('Musculo: ', mostro.musculo)

time.sleep(1)
print(' ')

print('Mais quero mais, Vamo mostro')
mostro.ficarGrandePorra(10)
time.sleep(0.5)
print('Musculo: ', mostro.musculo)

time.sleep(1)
print(' ')

print('Fica grande mostro poorraaa')
mostro.ficarGrandePorra(990)
time.sleep(0.5)
print('Musculo: ', mostro.musculo)
print(' ')
