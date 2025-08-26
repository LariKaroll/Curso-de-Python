#manipulando strings

curso = "pYtHon"

curso1 = " Python " 

curso2 = "Python"

print(curso.upper())  # Converte para maiúsculas
print(curso.lower())  # Converte para minúsculas
print(curso.title())  # Converte para título (primeira letra maiúscula de cada palavra)
print(curso1.strip())  # Remove espaços em branco no início e no final
print(curso1.lstrip())  # Remove espaços em branco no início
print(curso1.rstrip())  # Remove espaços em branco no final

#Juncoes e centralização
print(curso1.center(20, '*'))  # Centraliza a string com '*' até 20 caracteres
print("-".join(curso2))  # Junta os caracteres da string com '.'

