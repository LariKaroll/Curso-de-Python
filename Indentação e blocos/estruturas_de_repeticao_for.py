#estruturas de repetição
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

#exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
else:
    print("\nFim do loop")

#exemplo utilizando a funcao built-in range
for number in range(0,10): # loop de 0 a 9
    print(number, end=' ') #escreve o número na mesma linha