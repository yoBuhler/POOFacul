class Conta:
    def __init__(self, cpf, nome, saldo):
        self._cpf = cpf
        self._nome = nome
        self._saldo = saldo
        self._numero_alteracoes = 0

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        self._numero_alteracoes += 1
    
    @property
    def nome(self, nome):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        self._numero_alteracoes += 1

    @property
    def numero_alteracoes(self):
        return self._numero_alteracoes

    @numero_alteracoes.setter
    def numero_alteracoes(self, numero_alteracoes):
        self._numero_alteracoes = numero_alteracoes

    def deposita(self, valor):
        self._saldo += valor
        

c = Conta('1111', 'João', 1000.0)
print(c.numero_alteracoes)
c.cpf = '1111111'
print(c.numero_alteracoes)
c.nome = 'Maria'
print(c.numero_alteracoes)

class Veiculo:
    def __init__(self, modelo, ano, qtde_litros_no_tanque):
        self.__modelo = modelo
        self.__ano = ano
        self.__qtde_litros_no_tanque = qtde_litros_no_tanque

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def qtde_litros_no_tanque(self):
        return self.__qtde_litros_no_tanque

    @qtde_litros_no_tanque.setter
    def qtde_litros_no_tanque(self, qtde_litros_no_tanque):
        self.__qtde_litros_no_tanque = qtde_litros_no_tanque

    def abastecer(self, qtde):
        self.qtde_litros_no_tanque += qtde


v = Veiculo('celta', '2010', 12.0)

v.ano = '2010'
v.__ano = '2010'
