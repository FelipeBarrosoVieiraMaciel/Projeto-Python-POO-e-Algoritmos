from src.chapa import Chapa
from src.peca import Peca

class Encaixe:

    def __init__(self, chapa: Chapa = Chapa(0, 0), lista_pecas: list[Peca] = [], pecas_usadas: list[Peca] = []):
        self.chapa = chapa
        self.lista_pecas = lista_pecas
        self.pecas_usadas = pecas_usadas

    def encaixar_por_melhor(self, chapa: Chapa, ponto_inicial: list[int] = [0, 0], lista_pecas: list[Peca] = []):

        arquivo = 'output.txt'

        x, y = ponto_inicial[0], ponto_inicial[1]

        largura_chapa = chapa.largura
        altura_chapa = chapa.altura

        print(f'Chapa atual: {(chapa.largura, chapa.altura)}')

        lista_atual = lista_pecas.copy()
        lista_atual = self.invalidar_pecas(chapa, lista_atual) 
        
        # Caso base: Se após invalidar as peças para a chapa atual a lista de peças possíveis é vazia,
        # então devemos parar a execução
        if lista_atual == []:
            return
        
        melhor_largura = self.melhor_largura(chapa, lista_atual)
        melhor_altura = self.melhor_altura(chapa, lista_atual)
        
        melhor_resto = melhor_largura[1]
        melhor_peca = lista_atual[melhor_largura[0]]
        tipo_divisao = 'Largura'

        if melhor_altura[1] < melhor_resto:
            melhor_resto = melhor_altura[1]
            melhor_peca = lista_atual[melhor_altura[0]]
            tipo_divisao = 'Altura'

        print(f'Resto melhor largura: {melhor_largura[1]}')
        print(f'Resto melhor altura: {melhor_altura[1]}')
        print(f'Tipo de divisão {tipo_divisao}')

        if tipo_divisao == 'Largura': #Divisão por largura
            try:
                with open(arquivo, 'a') as file:
                    linha = str(f'{melhor_peca.tipo} {x} {y}\n') # Insere a melhor peça no começo da nossa nova chapa
                    file.write(linha)
            except FileNotFoundError:
                print('Arquivo não encontrado.')

            self.lista_pecas[melhor_largura[0]].quantidade -= 1 # Reduz a quantidade após o uso para não usarmos uma peça faltante

            print(f'Peça inserida: {melhor_peca.tipo} em divisão por {tipo_divisao}')
            self.pecas_usadas.append(melhor_peca)
            print(f'Criando a nova chapona: {largura_chapa, (altura_chapa - melhor_peca.altura)}')
            print(f'Posição inicial da chapona {x, y + melhor_peca.altura}')

            nova_chapona = Chapa(largura_chapa, (altura_chapa - melhor_peca.altura)) # (Lch, (Hch - Hi))
            pos_nova_chapona = [x, y + melhor_peca.altura] # (0x, 0y + Hi)

            self.encaixar_por_melhor(nova_chapona, pos_nova_chapona, lista_atual)

            print(f'Criando a nova chapinha: {(largura_chapa - melhor_peca.largura), melhor_peca.altura}')
            print(f'Posição inicial da chapinha {x + melhor_peca.largura, y}')

            nova_chapinha = Chapa((largura_chapa - melhor_peca.largura), melhor_peca.altura)
            pos_nova_chapinha = [x + melhor_peca.largura, y]

            print(f'Peça inserida: {melhor_peca.tipo} em divisão por {tipo_divisao} na chapa {(chapa.largura, chapa.altura)}')
            print(f'Criando a nova chapinha: {(largura_chapa - melhor_peca.largura), melhor_peca.altura}')

            self.encaixar_por_melhor(nova_chapinha, pos_nova_chapinha, lista_atual)

        else: #Divisão por altura
            try:
                with open(arquivo, 'a') as file:
                    linha = str(f'{melhor_peca.tipo} {x} {y}\n')
                    file.write(linha)
            except FileNotFoundError:
                print('Arquivo não encontrado.')

            self.lista_pecas[melhor_altura[0]].quantidade -= 1

            print(f'Peça inserida: {melhor_peca.tipo} em divisão por {tipo_divisao}')
            self.pecas_usadas.append(melhor_peca)
            print(f'Criando a nova chapona: {(largura_chapa - melhor_peca.largura), altura_chapa}')
            print(f'Posição inicial da chapona {x + melhor_peca.largura, y}')

            nova_chapona = Chapa((largura_chapa - melhor_peca.largura), altura_chapa)
            pos_nova_chapona = [x + melhor_peca.largura, y]

            self.encaixar_por_melhor(nova_chapona, pos_nova_chapona, lista_atual)

            print(f'Criando a nova chapinha: {melhor_peca.largura, (altura_chapa - melhor_peca.altura)}')
            print(f'Posição inicial da chapona {x, y + melhor_peca.altura}')

            nova_chapinha = Chapa(melhor_peca.largura, (altura_chapa - melhor_peca.altura))
            pos_nova_chapinha = [x, y + melhor_peca.altura]

            self.encaixar_por_melhor(nova_chapinha, pos_nova_chapinha, lista_atual)

    def melhor_largura(self, chapa: Chapa, lista_pecas: list[Peca]) -> list:
        
        menor_resto = chapa.largura % lista_pecas[0].largura
        pos_menor_resto = 0

        for i in range(len(lista_pecas)):

            if menor_resto == 0:
                return [pos_menor_resto, menor_resto]
       
            resto_atual = chapa.largura % lista_pecas[i].largura

            if resto_atual < menor_resto:
                menor_resto = resto_atual
                pos_menor_resto = i

        return [pos_menor_resto, menor_resto]
    

    def melhor_altura(self, chapa: Chapa, lista_pecas: list[Peca]) -> list:
        
        menor_resto = chapa.altura % lista_pecas[0].altura
        pos_menor_resto = 0

        for i in range(len(lista_pecas)):
            if menor_resto == 0:
                return [pos_menor_resto, menor_resto]

            resto_atual = chapa.altura % lista_pecas[i].altura

            if resto_atual < menor_resto:
                menor_resto = resto_atual
                pos_menor_resto = i

        return [pos_menor_resto, menor_resto]
        
    def maior_largura(self, lista_pecas: list[Peca]) -> int:

        maior = 0

        for i in range(len(lista_pecas)):
            if lista_pecas[i].largura > lista_pecas[maior].largura:
                maior = i

        return maior
    
    def maior_altura(self, lista_pecas: list[Peca]) -> int:

        maior = 0

        for i in range(len(lista_pecas)):
            if lista_pecas[i].altura > lista_pecas[maior].altura:
                maior = i

        return maior
    
    def invalidar_pecas(self, chapa: Chapa, lista_pecas: list[Peca]):

        # Se não tem peças, retorne a lista vazia para interromper logo a pilha
        if lista_pecas == []:
            return []

        for i in range(len(lista_pecas)):
            if lista_pecas[i].quantidade == 0:
                print(f'Peça do tipo {lista_pecas[i]} acabou')
                lista_pecas.pop(i)

        lista_valida = []

        for peca in lista_pecas:
            if peca.largura <= chapa.largura and peca.altura <= chapa.altura:
                lista_valida.append(peca)
            
        return lista_valida
    
    def area_usada(self, pecas_usadas: list[Peca] =[], area_total: int = 0):
        area_total = 0

        for peca in pecas_usadas:
            area_total = area_total + peca.calcula_area()
        return area_total
    