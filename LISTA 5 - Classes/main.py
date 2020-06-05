class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

class Quadrado:
    def __init__(self, sideSize):
        self.sideSize = sideSize

    def setSideSize(self, sideSize):
        self.sideSize = sideSize

    def getSideSize(self):
        return self.sideSize

    def getArea(self):
        return self.sideSize * self.sideSize

class Retangulo:
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
    
    def setSideA(self, sideA):
        self.sideA = sideA

    def setSideB(self, sideB):
        self.sideB = sideB

    def getSideA(self):
        return self.sideA

    def getSideB(self):
        return self.sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return self.sideA + self.sideB
        
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        self.altura = self.altura + 0.05 if self.idade < 21 else self.altura

    def engordar(self, kgs):
        self.peso += kgs

    def emagrecer(self, kgs):
        self.peso -= kgs
    
    def crescer(self, cms):
        self.altura += cms

class ContaCorrente:
    def __init__(self, accountNumber, accountHolder, amount = 0):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.amount = amount

    def changeHolder(self, accountHolder):
        self.accountHolder = accountHolder

    def addAmount(self, value):
        self.amount += value

    def lessAmount(self, value):
        self.amount -= value

class TV:
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume

    def setChannel(self, channel):
        if self.channel > 0 and self.channel <= 500:
            self.channel = channel
        else:
            print("Invalid Channel")

    def addVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume max")

    def lessVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume min")

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setFome(self, fome):
        self.fome = fome

    def setSaude(self, saude):
        self.saude = saude

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        self.bucho += alimento if self.bucho == '' else ' - ' + alimento

    def verBucho(self):
        print(self.nome + ' tem no bucho: ' +self.bucho)

    def digerir(self):
        self.bucho = ''

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print('X:' + str(self.x) + ' Y:' + str(self.y))

class NewRetangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def imprimir(self):
        print('Largura:' + str(self.largura) + ' Altura:' + str(self.altura))

    def retanguloMiddle(self):
        return Ponto(self.largura / 2, self.altura / 2)

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        if((valor / self.valorLitro) >= self.quantidadeCombustivel):
            self.quantidadeCombustivel -= (valor / self.valorLitro)
            print('Foi abastecido ' + str(valor / self.valorLitro) + ' de ' + self.tipoCombustivel)
        else:
            print('Não há esta quantidade de combustível disponivel')

    def abastecerPorLitro(self, quantidade):
        if(quantidade >= self.quantidadeCombustivel):
            self.quantidadeCombustivel -= quantidade
            print('Foi abastecido ' + str(quantidade) + ' de ' + self.tipoCombustivel)
        else:
            print('Não há esta quantidade de combustível disponivel')

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel


quadrado = Quadrado(5)
print(quadrado.getArea())

pessoa = Pessoa('johan', 17, 50, 1.41)
for i in range(5):
    pessoa.envelhecer()
    print(str(pessoa.altura) + " - " + str(pessoa.idade))

televisor = TV('SBT', 100)
televisor.addVolume()

alimentos = ['banana', 'maça', 'rollmops']
macacos = [Macaco('joãozinho', ''), Macaco('mariazinha', '')]
for alimento in alimentos:
    for macaco in macacos:
        macaco.comer(alimento)
        macaco.verBucho()

retangulo2 = NewRetangulo(50, 100)
print(retangulo2.retanguloMiddle().imprimir())