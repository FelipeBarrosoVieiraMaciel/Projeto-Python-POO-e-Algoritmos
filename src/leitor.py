from src.peca import Peca
from src.chapa import Chapa


class Leitor:

    def __init__(self, file, chapa: Chapa = Chapa(0, 0), numero: int = 0, pecas: list[Peca] = []):
        self.file = file
        self.chapa = chapa
        self.numero = numero
        self.pecas = pecas

    def ler_arquivo(self):
        arquivo = self.file
        
        try:

            with open(arquivo) as f:
                chapa = f.readline().split()

                self.chapa = self.criar_chapa(chapa)

                numero = f.readline()

                self.numero = int(numero)

                lista_pecas = []

                for i in range(int(numero)):
                    nova_peca = f.readline().split()

                    peca = self.criar_peca(nova_peca)

                    lista_pecas.append(peca)

                self.pecas = lista_pecas

        except FileNotFoundError:
            print('Arquivo não encontrado.')

    def criar_chapa(self, chapa) -> Chapa:
        return Chapa(int(chapa[0]), int(chapa[1]))

    def criar_peca(self, peca) -> Peca:
        return Peca(int(peca[0]), int(peca[1]), int(peca[2]), int(peca[3]))
    
    