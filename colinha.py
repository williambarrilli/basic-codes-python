#a = 5
#b = 6
#c = 2

#print("A",a > b) # A MAIOR QUE B
#print("B",a < c) # A É MENOR QUE C
#print("A",b == c) # B É IGUAL A C
#print("A",a > c < b)

#a = [1,2,3,4,5,6]

#b = [6,5,4,3,2,1,0]
#c = set(a).union(b) #Uni duas listas
#print(c)



#name = 'informatica'
#print(dir(name)) ############################## TESTA POSSIBILIDADES DO OBJETO
#print(name.lower().__doc__) ################# DESCREVE OQUE FAZ
#print("upper: ",name.upper()) # Maiusculo
#print("lower: ",name.lower()) # Minusculo
#print("capitalize: ",name.capitalize()) #Primeira letra Maiuscula
#print("title: ",name.title()) # Deixa a primeira letra Maiuscula das palavras
#print("swapcase: ",name.swapcase()) #
#print("startswith: ",name.startswith('p')) # checka se começa com 'p'
#print("Posição: ",name[0])
#print("Posição: ",name[:2])

#print(name[0] == 'i')
#print(name)
#aa = '123'
#bb,cc,dd = aa
#print(dd,cc,bb)
#print(name)

a = 'Programando em Python'

print(a[:a.find(' ')] +'iniciando' + a[a.find(' '):])
print(a.replace('',' inciando ',1))
