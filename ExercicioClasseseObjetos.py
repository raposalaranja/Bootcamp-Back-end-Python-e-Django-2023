#1. Crie uma classe que modele o objeto "carro".

#2. Um carro tem os seguintes atributos: ligado, cor, modelo,velocidade.

#3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,desacelera.

#4. Crie uma instância da classe carro.

#5. Faça o carro "andar" utilizando os métodos da sua classe.

#6. Faça o carro "parar" utilizando os métodos da sua classe

class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.velocidade_maxima = 250
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
        self.velocidade = 0

    def acelerar(self):
        if self.ligado == False:
         return
        
        if self.velocidade_maxima < self.limite:
            self.velocidade += 5

    def desacelerar(self):
        if self.ligado == False:
         return
        
        if self.velocidade > 0:
            self.velocidade_maxima = self.velocidade - 5
    

    @property #propriedades da classe carro
    def ligado(self):
        return self.ligado        
                 
    @property
    def cor(self):
        return self.cor

    @property
    def modelo(self):
        return self.modelo

    @property
    def velocidade(self):
        return self.velocidade
    
carro = Carro("branco", "Toyota") 
print(carro)