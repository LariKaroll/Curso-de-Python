salario = 2000

def calcular_bonus(bonus):
    global salario
    salario += bonus
    return salario

calcular_bonus(500)
print(salario)  # Exibe o salário atualizado com o bônus