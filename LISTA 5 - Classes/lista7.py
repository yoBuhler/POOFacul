class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(self.valor)

class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super.__init__()