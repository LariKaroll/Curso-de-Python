#estruturas condicionais

MAIOR_IDADE = 18

def verifica_idade(idade):
    if idade >= MAIOR_IDADE:
        print("Você é maior de idade.")
    elif idade < 0:
        print("Idade inválida.")
    else:
        print("Você é menor de idade.")
        
idade = int(input("Digite sua idade: "))
verifica_idade(idade)

#estrutura condicional aninhada
    #if dentro de if
    
#estrutura condicional ternária

status = "Maior de idade" if idade >= MAIOR_IDADE else "Menor de idade"
print(f"Você é {status}.")





