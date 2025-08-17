def sacar(valor): #inicio do bloco do metodo sacar
    saldo = 1000  # saldo inicial
    
    if saldo >= valor: #inicio do bloco if
        print(f"Saque de {valor} realizado com sucesso!")
        
        saldo -= valor # atualiza o saldo
        
        print(f"Saldo restante: {saldo}") 
        
    #fim do bloco if
#fim do bloco do metodo sacar

sacar(200)  # Chamada do método sacar com valor 200