from src.leitor import Leitor
from src.encaixe import Encaixe
from src.chapa import Chapa

class Main:

    entrada = 'input.txt'

    leitor = Leitor(entrada)

    leitor.ler_arquivo()

    chapa = leitor.chapa

    lista_pecas = leitor.pecas

    encaixe = Encaixe(chapa, lista_pecas)

    encaixe.encaixar_por_melhor(Chapa(chapa.largura, chapa.altura), [0, 0], lista_pecas)

    area_chapa = chapa.calcula_area()

    area_usada = encaixe.area_usada(encaixe.pecas_usadas)

    print(f'Área usada = {area_usada}')
    print(f'Área chapa = {area_chapa}')
    print(f'Aproveitamento = {area_usada / area_chapa * 100}%')

   
    
   