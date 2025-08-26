#metodos que existem em dicionarios

pessoa = {
    "01": {"nome": "Larissa", "idade": 21, "altura": 1.65, "cidade": "Brasilia", "profissao": "Programadora"},
    "02": {"nome": "João", "idade": 20, "altura": 1.80, "cidade": "São Paulo", "profissao": "Engenheiro"},
    "03": {"nome": "Ana", "idade": 22, "altura": 1.70, "cidade": "Rio de Janeiro", "profissao": "Designer"},
    "04": {"nome": "Carlos", "idade": 23, "altura": 1.75, "cidade": "Belo Horizonte", "profissao": "Médico"},
}

pessoa.update({"05": {"nome": "Maria", "idade": 19, "altura": 1.60, "cidade": "Curitiba", "profissao": "Estudante"}})  # Adicionando nova pessoa
pessoa.get("01")  # Obtendo os dados da pessoa com chave "01"
pessoa.get("06", "Pessoa não encontrada")  # Tentando obter uma chave inexistente com valor padrão
pessoa.pop("02")  # Removendo a pessoa com chave "02"
pessoa.keys()  # Obtendo todas as chaves do dicionário
pessoa.values()  # Obtendo todos os valores do dicionário
pessoa.items()  # Obtendo todos os itens (chave-valor) do dicionário
pessoa.fromkeys(["06", "07"], {"nome": "Desconhecido", "idade": 0, "altura": 0.0, "cidade": "Desconhecida", "profissao": "Desconhecida"})  # Criando novas chaves com valores padrão
pessoa.setdefault("08", {"nome": "Lucas", "idade": 25, "altura": 1.85, "cidade": "Porto Alegre", "profissao": "Professor"})  # Adiciona se a chave não existir e se existir, retona o valor existente
pessoa.popitem()  # Remove e retorna o último item adicionado (chave-valor)
pessoa.values()  # Retorna todos os valores do dicionário

telefone = "telefone" in pessoa["01"]
print(telefone)  # Verifica se a chave "telefone" existe no dicionário da pessoa com chave "01"

profissao = "profissao" in pessoa["03"]
print(profissao)  # Verifica se a chave "profissao" existe no dicionário da pessoa com chave "03"

pessoa.copy()  # Fazendo uma cópia do dicionário

pessoa.clear()  # Limpando todos os dados do dicionário