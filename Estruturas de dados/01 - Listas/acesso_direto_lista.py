frutas = ["maçã", "banana", "laranja", "uva"]

print(frutas[0])  # Acesso ao primeiro elemento
print(frutas[1])  # Acesso ao segundo elemento
print(frutas[-1])  # Acesso ao último elemento
print(frutas[-2])  # Acesso ao penúltimo elemento

for fruta in frutas:
    print(fruta)  # Iterando sobre a lista e imprimindo cada fruta
    
indece = 0
for indece, fruta in enumerate(frutas):
    print(f"Fruta {indece}: {fruta}")  # Imprimindo o índice e a fruta correspondente
    


num1 = input()
num2 = input()
print(int(num1) + int(num2))  # Concatenando strings

lista_comprehension = [n**2 if n > 8 else n for n in range(10)]  # List comprehension com condição
print(lista_comprehension)  # Imprimindo a lista resultante