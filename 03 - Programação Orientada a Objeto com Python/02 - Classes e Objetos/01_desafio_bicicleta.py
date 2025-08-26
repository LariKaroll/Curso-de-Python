class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    #self = instancia da propria classe para os objetos
    #__init__ = construtor
    
    def __del__(self):
        print(f"Modelo Removido -> {self.modelo}")
    
    def buzinar(self):
        print("Plim, Plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")
    
    def correr(self):
        print("Vrummmm...")
        
    def __str__(self):
        return f"{self.__class__.__name__} -> {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

b1 = Bicicleta("vermelha", "caloi", 2022, 700)
b1.buzinar()
b1.correr()
b1.parar()

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)


    
