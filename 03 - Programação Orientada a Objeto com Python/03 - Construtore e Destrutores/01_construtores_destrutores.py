class Cachorro:
    #construtor
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    #Executado no final
    def __del__(self):
        print("Removendo a instância da classe.")
        
    def falar(self):
        print("AUAUAU...")
        
c = Cachorro("Charle", "verde")
c.falar()

