import matplotlib.pyplot as plt
import matplotlib.patches as patches

def visualizar_cortes(largura_chapa, altura_chapa, dimensoes_pecas, arquivo_saida='output.txt'):
    """
    largura_chapa, altura_chapa: Dimensões originais da chapa principal.
    dimensoes_pecas: Dicionário mapeando o 'tipo' da peça para uma tupla (largura, altura).
                     Ex: {1: (108, 76), 2: (110, 43), 3: (92, 81)}
    """
    # Cria a figura e os eixos
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Desenha a chapa principal (fundo cinza claro)
    chapa_principal = patches.Rectangle((0, 0), largura_chapa, altura_chapa, 
                                        linewidth=2, edgecolor='black', facecolor='#e0e0e0')
    ax.add_patch(chapa_principal)

    cores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    try:
        with open(arquivo_saida, 'r') as file:
            for linha in file:
                # O arquivo tem o formato: tipo x y
                partes = linha.strip().split()
                if len(partes) == 3:
                    tipo = int(partes[0])
                    x = float(partes[1])
                    y = float(partes[2])
                    
                    if tipo in dimensoes_pecas:
                        largura, altura = dimensoes_pecas[tipo]
                        cor = cores[tipo % len(cores)] # Escolhe uma cor baseada no tipo
                        
                        # Desenha a peça
                        peca = patches.Rectangle((x, y), largura, altura, 
                                                 linewidth=1, edgecolor='black', facecolor=cor, alpha=0.8)
                        ax.add_patch(peca)
                        
                        # Adiciona o texto no centro da peça
                        ax.text(x + largura/2, y + altura/2, f'T:{tipo}', 
                                color='black', weight='bold', fontsize=8, ha='center', va='center')

    except FileNotFoundError:
        print(f"Arquivo '{arquivo_saida}' não encontrado. Rode seu algoritmo primeiro!")
        return

    # Ajusta os limites do gráfico para caber a chapa com uma margem
    ax.set_xlim(-10, largura_chapa + 10)
    ax.set_ylim(-10, altura_chapa + 10)
    ax.set_aspect('equal') # Mantém a proporção real entre x e y
    
    plt.title(f'Visualização do Corte Bidimensional (Chapa {largura_chapa}x{altura_chapa})')
    plt.xlabel('Eixo X (Comprimento)')
    plt.ylabel('Eixo Y (Altura)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# --- COMO USAR ---
# 1. Defina as dimensões da chapa que você usou no seu teste (ex: a do PDF)
LARGURA_CHAPA = 587
ALTURA_CHAPA = 233

# 2. Mapeie os tipos de peças com suas respectivas larguras e alturas
# Formato: { tipo: (largura, altura) }
PECAS_DICT = {
    1: (108, 76),
    2: (110, 43),
    3: (92, 81)
}

# 3. Chame a função após o seu código de Encaixe ter gerado o output.txt
visualizar_cortes(LARGURA_CHAPA, ALTURA_CHAPA, PECAS_DICT)