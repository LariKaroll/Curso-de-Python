#O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.

def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador ={}
#TODO: Itere através de cada caractere na string string.
    for char in string:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    
    return contador

# Solicita entrada do usuário
entrada = input("Digite uma string: ")
resultado = contar_caracteres(entrada)
print(resultado)