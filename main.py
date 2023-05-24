import random
import matplotlib.pyplot as plt

def calcular_aptidao(cromossomo):
    x = int(''.join(map(str, cromossomo)), 2)
    return x / 2

def criar_populacao(tamanho_populacao, tamanho_cromossomo):
    populacao = []
    for _ in range(tamanho_populacao):
        cromossomo = [random.randint(0, 1) for _ in range(tamanho_cromossomo)]
        populacao.append(cromossomo)
    return populacao

def selecionar_pais(populacao):
    pais = random.sample(populacao, 2)
    return pais

def cruzamento(pais):
    ponto_corte = random.randint(1, len(pais[0]) - 1)
    filho1 = pais[0][:ponto_corte] + pais[1][ponto_corte:]
    filho2 = pais[1][:ponto_corte] + pais[0][ponto_corte:]
    return filho1, filho2

def mutacao(individuo, probabilidade_mutacao, mutacao_fixa=False):
    if mutacao_fixa:
        gene = random.randint(0, len(individuo) - 1)
        individuo[gene] = 1 - individuo[gene]
    else:
        for i in range(len(individuo)):
            if random.random() < probabilidade_mutacao:
                individuo[i] = 1 - individuo[i]
    return individuo

def media_aptidao(populacao):
    aptidoes = [calcular_aptidao(individuo) for individuo in populacao]
    return sum(aptidoes) / len(aptidoes)

def melhor_individuo(populacao):
    aptidoes = [calcular_aptidao(individuo) for individuo in populacao]
    indice_melhor = aptidoes.index(max(aptidoes))
    return populacao[indice_melhor]

def mostrar_grafico(media_aptidoes, melhores_aptidoes):
    geracoes = range(len(media_aptidoes))
    plt.plot(geracoes, media_aptidoes, label='Média de Aptidão')
    plt.plot(geracoes, melhores_aptidoes, label='Melhor Aptidão')
    plt.xlabel('Geração')
    plt.ylabel('Aptidão')
    plt.legend()
    plt.show()

def mostrar_populacao(populacao):
    for i, individuo in enumerate(populacao):
        print(f'Indivíduo {i + 1}: {individuo}')

def algoritmo_genetico(
    tamanho_populacao,
    tamanho_cromossomo, 
    probabilidade_cruzamento,
    probabilidade_mutacao, 
    mutacao_fixa, num_geracoes
    ):
    populacao = criar_populacao(tamanho_populacao, tamanho_cromossomo)
    media_aptidoes = []
    melhores_aptidoes = []
    
    for geracao in range(num_geracoes):
        nova_populacao = []
        
        for _ in range(tamanho_populacao // 2):
            pais = selecionar_pais(populacao)
            filho1, filho2 = cruzamento(pais)
            
            filho1 = mutacao(filho1, probabilidade_mutacao, mutacao_fixa)
            filho2 = mutacao(filho2, probabilidade_mutacao, mutacao_fixa)
            
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao
        
        media_aptidao_atual = media_aptidao(populacao)
        melhor_aptidao_atual = calcular_aptidao(melhor_individuo(populacao))
        
        media_aptidoes.append(media_aptidao_atual)
        melhores_aptidoes.append(melhor_aptidao_atual)
        
    mostrar_grafico(media_aptidoes, melhores_aptidoes)
    mostrar_populacao(populacao)

# Parâmetros de entrada
tamanho_populacao = 10
tamanho_cromossomo = 20
probabilidade_cruzamento = 0.8
probabilidade_mutacao = 0.1
mutacao_fixa = True
num_geracoes = 50

# Executar o algoritmo genético
algoritmo_genetico(tamanho_populacao, tamanho_cromossomo, probabilidade_cruzamento,
                   probabilidade_mutacao, mutacao_fixa, num_geracoes)
