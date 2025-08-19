#declarnado dicionario

pessoa = {
    "nome" : "Larissa",
    "idade" : 21,
    "altura" : 1.65,
    "cidade" : "Brasilia",
    "profissao" : "Programadora",
}

print(pessoa)  # Imprimindo o dicionário completo
print(pessoa["nome"],pessoa["idade"])  # Acessando valores específicos usando chaves

#adicionar novo valor ao dicionário
pessoa["pais"] = "Brasil"  # Adicionando uma nova chave-valor
print(pessoa)

pessoas = dict(nome = "Joao", idade = 20, profissao = "Lutador")  # Declarando um dicionário 