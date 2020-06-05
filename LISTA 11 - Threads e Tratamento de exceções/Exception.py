class NotMyName(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


def guess_my_name():
    print('Qual é o seu nome?')
    name = input()
    if name != 'Johan Mickael Kneubuhler':
        raise NotMyName('O nome: {}'.format(name) + ' é diferente de Johan Mickael Kneubuhler')

while True:
    try:
        guess_my_name()
        print('sucesso!')
        break
    except NotMyName:
        print('Nome incorreto')