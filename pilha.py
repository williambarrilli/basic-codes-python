class Pilha:
    def __init__(self): #Lista interna
        self._vet = []

    def push(self,item): # Metodo de inserir item
        self._vet.append(item)

    def pop(self): #Remover o topo
        #Tratar underflow
        if self.is_empty != True:
            return self._vet.pop()
        else:
            print("Pilha Vazia")

    def is_empty(self): # Teste se � vazia
        if len(self._vet) == 0:
            return True
        else:
            return False

    def size (self): # Retorna o total de itens
        return len(self._vet)

### TESTES ###
p1 = Pilha()
p2 = Pilha()

p1.push("carta1")
p1.push("carta2")
p1.push("carta3")
print(p1.size())
print(p1.pop())
print(p1.pop())
print(p1.pop())
