tupla = (1,2,3,4,5) # Declarando uma tupla com 5 elementos

#a tupla diferente de uma lista, nao pode ser alterada , ou seja, é imutavel
#Outra coisa a Lista e formada por colchetes[] e a tupla por parenteses()

print(tupla)  # Imprimindo a tupla

tupla.count(1)  # Contando quantas vezes o número 1 aparece na tupla
tupla.index(3)  # Encontrando o índice do número 3 na tupla
len(tupla)  # Obtendo o tamanho da tupla

#tupla[0] = 10  # Tentativa de alterar o primeiro elemento da tupla (isso causará um erro)  

carros = ("gol") 
print(isinstance(carros, tuple))  