from threading import Thread
from random import randint

DISTANCIA = 20
CLASSIFICACAO = []

class Rabbit(Thread):
    def __init__(self, numero):
        Thread.__init__(self)
        self.qtdePulos = 0
        self.distanciaPercorrida = 0
        self.numero = numero

    def run(self):
        while start != True:
            print('Aguardando outras lebres')
        else:
            while self.distanciaPercorrida < DISTANCIA:
                pulo = randint(1, 3)
                print('A lebre ' + str(self.numero) + ' pulou ' + str(pulo) + ' metros')
                self.qtdePulos += 1
                self.distanciaPercorrida += pulo
            
            print('A lebre ' + str(self.numero) + ' chegou')
            CLASSIFICACAO.append(self)

def sortRabbits_qtdePulos(rabbit):
    return rabbit.qtdePulos


start = False
rabbits = [Rabbit(1), Rabbit(2), Rabbit(3), Rabbit(4), Rabbit(5)]
for rabbit in rabbits:
    rabbit.start()

start = True

for rabbit in rabbits:
    rabbit.join()

print('Lebre que deu menos saltos: ' + str(sorted(rabbits, key=sortRabbits_qtdePulos)[0].numero))
print('Classificação:')
for rabbit in CLASSIFICACAO:
    print('Lebre: ' + str(rabbit.numero) + ', quantidade de saltos:' + str(rabbit.qtdePulos))