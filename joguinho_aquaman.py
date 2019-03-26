from random import shuffle
import os

class Carta():
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __eq__(self, other):
        return self.valor == other.valor and self.naipe == other.naipe

    def imprime_carta(self):
        return '{} de {}'.format(self.valor, self.naipe)

    def __str__(self):
        return self.imprime_carta()

    def __repr__(self):
        return self.imprime_carta()

class Baralho(Carta):
    lista1 = []
    lista2 = []
    player1 = 0
    player2 = 0
    def __init__(self):
        naipes = ['copa','espada','ouro','bastos']
        valores = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.cartas = [Carta(v,n) for n in naipes for v in valores]

    def embaralhar(self):
        shuffle(self.cartas)

    def encontrar_carta(self,carta):
        x = self.cartas.index(carta)
        return x

    def is_empty(self):
        if len(self.lista1 or self.lista2) == 0:
            return True
        else:
            return False

    def dividir_carta(self,numero_pessoa):
        divisao = len(self.cartas) / numero_pessoa

        for i in range(0,int(divisao)):
            x = self.cartas.pop()
            self.lista1.append(x)
            y = self.cartas.pop()
            self.lista2.append(y)

    def tabelo_pontos(self):
        print('Tabela De Pontos\nJogador1:',self.player1,'Jogador2:',self.player2,'\n')

    def batalha(self):
        pessoa1 = self.lista1.pop()
        pessoa2 = self.lista2.pop()
        print('Jogador 1: ',pessoa1,'\nJogador 2: ', pessoa2)
        if pessoa1.valor > pessoa2.valor:
            self.player1 += 1
            return ('\n>>>Jogador 1 ganho<<<\n')
        elif pessoa2.valor > pessoa1.valor:
            self.player2 += 1
            return ('\n>>>Jogador 2 ganho<<<\n')
        elif pessoa1.valor == pessoa2.valor:
            return ('\n>>>empatou!<<<\n')


##########FROOOOOOOOOOOOOOOOOOOOONT#################


print('JOGO DO CARINHA DO AQUAMAN')
deck = Baralho()
deck.embaralhar()
deck.dividir_carta(2)
while True:
    print("Digite:\n1 - Batalhar\n0 - Sair")
    menu = input()
    if menu == '1':
        print(deck.batalha())
        deck.tabelo_pontos()
        if deck.is_empty()==True:
            print('ACABOU AS CARTAS!!!')
            break
    elif menu == '0':
        exit()
    elif menu != '0' or '1':
        print('Opção Invalida!')
