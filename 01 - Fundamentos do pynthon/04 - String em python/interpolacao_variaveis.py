#interpolacao 

nome = "Larissa"
idade = 21
profissao = "programadora"
linguagem = "Python"
saldo = 1000.2131

#dicionario
dados = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": linguagem
}

#metodo com %
print("Meu nome é %s, tenho %d anos, sou %s e estou aprendendo %s." % (nome, idade, profissao, linguagem))

#metodo com format
print("Meu nome é {}, tenho {} anos, sou {} e estou aprendendo {}.".format(nome, idade, profissao, linguagem))
print("Meu nome é {0}, tenho {1} anos, sou {2} e estou aprendendo {3}.".format(nome, idade, profissao, linguagem))

print("Meu nome é {nome}, tenho {idade} anos, sou {profissao} e estou aprendendo {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#metodo format com dicionario]

print("Meu nome é {nome}, tenho {idade} anos, sou {profissao} e estou aprendendo {linguagem}.".format(**dados))

#metodo com F
print(f"Meu nome é {nome}, tenho {idade} anos, sou {profissao} e estou aprendendo {linguagem}. Saldo: R${saldo:10.3f}")