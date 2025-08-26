def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    
    contador = 0
    
    for char in texto:
        if char in vogais:
            contador += 1
    return contador
    

texto = input("digite um texto: ")

resultado = conta_vogais(texto)
print(f"O numero de vogais na string '{texto}' é: {resultado}")