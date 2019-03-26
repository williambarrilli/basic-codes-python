class Animal():
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def get_nome(self):
        return self.nome


class Mamiferos(Animal):
    pass


class Aves():
    def __init__(self, ovos, bicos):
        self.ovos = ovos
        self.bicos = bicos


class Voador():
    def __init__(self, asas):
        self.asas = asas


class Mamador():
    def __init__(self, mamas):
        self.mamas = mamas

# animais


class Gato(Mamiferos, Mamador):
    def __init__(self,mamiferos,mamador, pelagem):
        self.mamiferos = mamiferos
        self.mamador = mamador
        self.pelagem = pelagem


animal = Mamiferos('Mamifero', '2')
mamiferos = Mamiferos('gatao','5')
mamador = Mamador('2 mamas')
gato = Gato(mamiferos,mamador,'pelagem escura')
print(animal.tamanho)
