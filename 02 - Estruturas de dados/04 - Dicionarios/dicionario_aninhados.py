contatos = {
    "bebeb@gmail.com":{"nome": "Bebê", "idade": "21","telefone": "1844-5128"},
    "lari@gmail.com":{"nome": "Larissa", "idade": "24","telefone": "1934-5478"},
    "gabri@gmail.com":{"nome": "Gabriela", "idade": "22","telefone": "1214-5671"},
    "milek@gmail.com":{"nome": "Milek", "idade": "23","telefone": "1234-5678"},
}

for chave, valor in contatos.items():
    print(f"Email: {chave}, Nome: {valor['nome']}, Idade: {valor['idade']}, Telefone: {valor["telefone"]}")  