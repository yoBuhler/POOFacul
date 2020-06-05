# from threading import Thread
# from random import randint

# chegada = 20
# ranking = []


# class Lebre(Thread):
#     def __init__(self, numero):
#         Thread.__init__(self)
#         self.quantidadePulos = 0
#         self.distanciaPercorrida = 0
#         self.numero = numero

#     def run(self):
#         while largar != True:
#             print('Esperando a largada')
#         else:
#             while self.distanciaPercorrida < chegada:
#                 salto = randint(1, 3)
#                 print('A lebre {} saltou {} metros'.format(self.numero, salto))
#                 self.quantidadePulos += 1
#                 self.distanciaPercorrida += salto

#             print('A lebre {} finalizou a corrida'.format(self.numero))
#             ranking.append(self)


# def sortLebres_quantidadePulos(lebre):
#     return lebre.quantidadePulos


# largar = False
# lebres = [Lebre(1), Lebre(2), Lebre(3), Lebre(4), Lebre(5)]
# for lebre in lebres:
#     lebre.start()

# largar = True

# for lebre in lebres:
#     lebre.join()

# print('Lebre que deu menos saltos: {}'.format(
#     sorted(lebres, key=sortLebres_quantidadePulos)[0].numero))
# print('Classificação:')
# for lebre in ranking:
#     print('Lebre: {}, quantidade de saltos: {}'.format(
#         lebre.numero, lebre.quantidadePulos))


# from threading import Thread
# from random import randint

# class soma(Thread):
#     def __init__(self, numeros):
#         Thread.__init__(self)
#         self.numeros = numeros
#         self.subTotal = 0

#     def run(self):
#         for number in self.numeros:
#             self.subTotal += number


# numeros = []
# for i in range(1000):
#     numeros.append(randint(0, 9999))

# somas = [soma(numeros[0:250]), soma(numeros[251:500]), soma(numeros[501:750]), soma(numeros[751:1000])]

# for soma in somas:
#     soma.start()

# for soma in somas:
#     soma.join()

# total = 0
# for soma in somas:
#     total += soma.subTotal

# print('O total da soma é: {}'.format(total))


# class NotMyName(Exception):
#     def __init__(self, message):
#         Exception.__init__(self)
#         self.message = message


# def guess_my_name():
#     print('qual o seu nome?')
#     name = input()
#     if name != 'Ingrid Ester Zimmermann Morsch':
#         raise NotMyName('O nome: {} não é igual a Ingrid Ester Zimmermann Morsch'.format(name))

# while True:
#     try:
#         guess_my_name()
#         print('sucesso!')
#         break
#     except NotMyName:
#         print('nome incorreto')
