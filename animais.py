class Animal():
    def __init__(self,nome,tamanho):
        self.nome = nome
        self.tamanho = tamanho


class Mamifero(Animal):
    '''
    nome,tamanho
    '''
    def __init__(self,nome,tamanho):
        super().__init__(nome,tamanho)

class Mamas(Mamifero):
    def __init__(self,nome, tamanho, mamas):
        super().__init__(nome,tamanho)
        self.mamas = mamas

class Voador():
    def __init__(self, asas):
        self.asas = asas

class Gato(Mamas):
    def __init__(self,nome,tamanho,mamas,numero_patas):
        super().__init__(nome,tamanho,mamas)
        self.numero_patas = numero_patas

class Cachorro(Mamas):
    def __init__(self, nome, tamanho, mamas, unhas):
        super().__init__(nome,tamanho,mamas)
        self.unhas= unhas

class Coelho(Mamas):
    def __init__(self, nome, tamanho, mamas, rabo):
        super().__init__(nome, tamanho, mamas)
        self.rabo = rabo

class Aves(Animal, Voador):
    def __init__(self, nome, tamanho, ovos, bico,asas):
        Animal.__init__(self,nome, tamanho)
        Voador.__init__(self,asas)
        self.ovos = ovos
        self.bico = bico

class Canarinho(Aves):
    pass

class Morcego(Voador, Mamas):
    def __init__(self, asas,nome,tamanho,mamas):
        Voador.__init__(self,asas)
        Mamas.__init__(self,nome,tamanho,mamas)

    def __str__(self):
        return '{} {} {} {}'.format(self.asas, self.nome,self.tamanho,self.mamas)

class Ornitorrinco():
    def __init__(self, nome, tamanho, ovos, bico):
        self.nome = nome
        self.tamanho =tamanho
        self.ovos = ovos
        self.bico = bico

gato = Gato('rodolfo','5 tamanho','2 mamas','4 patas')
cachorro= Cachorro('rex','7 tamanho' , '8 mamas', 'unhas pretas')
coelho = Coelho('pimpom', '2 tamanho', '8 mamas', 'rabo curto')
canarinho= Canarinho('piupiu', '2','2', 'bico amarelo','asa azul')
morcego = Morcego('2 asas','morcego','1 tamanho','2 mamas')
ornitorrinco = Ornitorrinco('perry','50 cm', '2', 'bico amarelo')
print(gato)
print(canarinho)
print(ornitorrinco)
