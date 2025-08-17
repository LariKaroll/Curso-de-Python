#estruturas de repetição
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"
contador = 0

#exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        contador += 1
        print(letra, end=' ')
else:
    print("\nFim do loop")
    
print(contador)

#exemplo utilizando a funcao built-in range
for number in range(0,10): # loop de 0 a 9
    print(number, end=' ') #escreve o número na mesma linha