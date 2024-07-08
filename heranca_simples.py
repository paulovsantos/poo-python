class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    #métodos 
    def ligar_motor(self):
        print('Ligando o moto')
        
    #def __str__(self):
        #return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
    def __str__(self):
          return self.cor
        
class Motocicleta(Veiculo):
        pass
    
class Carro(Veiculo):
        pass
    
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
            super().__init__(cor, placa, numero_rodas)
            self.carregado = carregado
            
    def esta_carregado(self):
            print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
                
    #instanciar
moto = Motocicleta("preta", "PVS-123", 2)
carro = Carro("prata", "LLK-9767", 4)
caminhao = Caminhao("roxo", "GVX-1234", 10, True)

print(moto)
print(carro)
print(caminhao)

    