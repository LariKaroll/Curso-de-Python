lista = [1,2,2,3,4,5, 2, 3, 4, 5]  # Declarando uma lista com 5 elementos

#para declarar um conjunto, usamos a função set()
conjuntos = set(lista)  # O set() remove duplicatas e cria um conjunto
print(lista)  # Imprimindo a lista original
print(conjuntos)  # Imprimindo o conjunto
conjunto = {1, 2, 3, 4, 5} # Declarando um conjunto com elementos
conjunto2 = {2,9,4,1,8}  # Declarando outro conjunto com elementos

#obs

# Conjuntos nao podem ser fatiados ou seja, nao podemos acessar um elemento especifico
# Portanto devemos transformar o conjunto em uma lista para acessar um elemento especifico

numb = {1,2,3,4,5}
numbs = list(numb)
print(numbs[0])  # Acesso ao primeiro elemento do conjunto convertido em lista


# Metodos

conjunto.union(conjunto2)  # União dos dois conjuntos
conjunto.intersection(conjunto2)  # Interseção dos dois conjuntos
conjunto.difference(conjunto2)  # Diferença entre os dois conjuntos
conjunto.symmetric_difference(conjunto2)  # Diferença simétrica entre os dois conjuntos
conjunto.issubset(conjunto2)  # Verifica se conjunto é subconjunto de conjunto2
conjunto.issuperset(conjunto2)  # Verifica se conjunto é superconjunto de conjunto2
conjunto.isdisjoint(conjunto2)  # Verifica se os conjuntos são disjuntos (não têm elementos em comum)
conjunto.add(6)  # Adiciona o elemento 6 ao conjunto
conjunto.remove(2)  # Remove o elemento 2 do conjunto (gera erro se não existir)
conjunto.discard(3)  # Remove o elemento 3 do conjunto (não gera erro se não existir)
conjunto.clear()  # Limpa todos os elementos do conjunto
conjunto.copy()  # Cria uma cópia do conjunto
#conjunto.pop()  # Remove e retorna um elemento aleatório do conjunto (gera erro se o conjunto estiver vazio)
print(len(conjunto))  # Retorna o número de elementos no conjunto
print(2 in conjunto)  # Verifica se o elemento 2 está no conjunto