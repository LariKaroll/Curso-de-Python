def calcular_total(num):
    return sum(num)

def retonar_antecessor_e_sucessor(num):
    antecessor = num - 1
    sucessor = num + 1
    return antecessor, sucessor

print(calcular_total([2,2,2,2]))
print(retonar_antecessor_e_sucessor(190))