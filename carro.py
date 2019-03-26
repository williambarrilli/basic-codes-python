import time as th

class Carro():

   def __init__(self, velocidade_maxima, velocidade_atual=0):
       self.velocidade_maxima = velocidade_maxima
       self.velocidade_atual = velocidade_atual

   def acelerar(self, aceleracao):
       acelerando = True
       while acelerando:
           if self.velocidade_atual >= self.velocidade_maxima:
               print("{} m/s".format(self.velocidade_maxima))
               self.velocidade_atual = self.velocidade_maxima
               acelerando = False
           else:
               th.sleep(1)
               print("{} m/s".format(self.velocidade_atual))
               self.velocidade_atual += aceleracao

            if self.velocidade_atual >= self.velocidade_maxima:
                th.sleep(1)
                print("{} m/s".format(self.velocidade_atual))
                self.velocidade_atual += aceleracao
            else:
                print("{} m/s".format(self.velocidade_maxima))
                self.velocidade_atual = self.velocidade_maxima
                acelerando = False

   def frear(self, aceleracao):
       desacelerando = True
       while desacelerando:
           if self.velocidade_atual <= 0:
               self.velocidade_atual = 0
               print("{} m/s".format(self.velocidade_atual))
               desacelerando = False
           else:
               th.sleep(1)
               print("{} m/s".format(self.velocidade_atual))
               self.velocidade_atual -= aceleracao

carro = Carro(240)
carro.acelerar(20)
print("\n Velocidade do Carro: {} m/s\n".format(carro.velocidade_atual))
carro.frear(20)
print("\n Velocidade do Carro: {} m/s\n".format(carro.velocidade_atual))
