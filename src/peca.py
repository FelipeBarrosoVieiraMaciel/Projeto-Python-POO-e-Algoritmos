class Peca:

    def __init__(self, tipo, largura, altura, quantidade: int):
        self.tipo = tipo
        self.largura = largura
        self.altura = altura
        self.quantidade = quantidade

    def calcula_area(self) -> int:
        return self.largura * self.altura
    
    def calcula_area_total(self):
        return self.calcula_area() * self.quantidade
    