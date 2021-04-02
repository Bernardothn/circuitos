import sys
import cmath

tamanho = int(input("Insira o tamanho da matriz quadrada e \nposteriormente cada elemento de suas linhas: "))
matriz = []
vetorB = []
vetorC = [None]*tamanho
vetorS = [None]*tamanho

"Essa função cria a matriz de entrada."


def cria_matriz(qtd, matriz):
    for i in range(qtd):
        print(f'Por favor, digite a {i}-ésima linha: ')
        linha = list()
        for j in range(qtd):
            elemento = complex(input())
            linha.append(elemento)
        matriz.append(linha)
    return matriz


"Essa função cria o vetor independente. 'O vetor da direita'. "


def cria_vetor(qtd, vetor):
    for i in range(qtd):
        elemento = complex(input())
        vetor.append(elemento)
    return vetor


"Essa função imprime as matrizes de entrada e LU."


def imprime_matriz(valores):
    for i in range(len(valores)):
        for j in range(len(valores[i])-1):
            print((valores[i][j]), end=" ")
        print(valores[i][len(valores[i])-1], end="\n")
    return None


"Essa função imprime os vetores de entrada e solução."


def imprime_vetor(vetor):
    for i in range(len(vetor)):
        print(vetor[i])
    return None


"Essa função auxiliar troca as colunas especificadas em maior_coluna. " \
"Aqui troca-se a primeira linha da k-ésima matriz pela linha que contém o maior " \
"elemento da k-ésima coluna."


def troca_linha(matriz, vetor_linha, linhadomaior, k):
    matriz[k], matriz[linhadomaior] = matriz[linhadomaior], matriz[k]
    vetor_linha[k], vetor_linha[linhadomaior] = vetor_linha[linhadomaior], vetor_linha[k]     # Repara que, ao
    # operar a substituição na matriz, deve-se executar no vetor de entrada (vetor_linha).
    return None


"Essa função encontra o maior elemento da coluna k."


def maior_coluna(matriz, vetor_linha, k):
    mc = matriz[k][k]          # mc significa o maior elemento da coluna. Nesse caso, no início da
    # k-ésima matriz ou k-ésima linha e coluna da matriz original.
    linhadomaior = k           # Supomos que mc é o primeiro da k-ésima matriz e, obviamente, está na k-ésima
    # linha da matriz de entrada.
    for linha in range(k, tamanho):          # Itera-se sobre as linhas da k-ésima matriz.
        if abs(matriz[linha][k]) > abs(mc):          # Ocorre a troca do maior da coluna.
            mc = matriz[linha][k]
            linhadomaior = linha
    troca_linha(matriz, vetor_linha, linhadomaior, k)          # Chama a função para operar a troca única de linhas.
    return None


"Essa função escalona a matriz da coluna k até a última da direita."


def escalonamento(matriz, k):
    pivo = matriz[k][k]          # Primeiro elemento da diagonal da matriz k-ésima.
    for linha in range(k+1, tamanho):          # Itera sobre as linhas que vem embaixo.
        primeirodalinha = matriz[linha][k]
        for coluna in range(k, tamanho):          # Ocorre a eliminação gaussiana
            matriz[linha][coluna] = matriz[linha][coluna] - (matriz[k][coluna]*primeirodalinha/pivo)     # Multiplica
            # a primeira linha da matriz k-ésima pelo fator especificado e depois soma com as demais linhas.
            matriz[linha][k] = primeirodalinha/pivo        # Esse elemento guarda as operações na matriz L.
    return matriz


"Essa função de fato faz a decomposição LU da matriz. Tudo por meio de sucessivas " \
"k (tamanho da matriz) repetições que são possibilitadas pelas funções maior_coluna e escalonamento."


def decomposicao_lu(matriz, vetor_linha):
    for k in range(tamanho-1):   # Aqui ocorre a iteração sobre as linhas da matriz. Repara que para k=0,
        # temos a matriz de entrada; para k=1, temos a matriz de entrada exceto a primeira linha e coluna; para k=2,
        # matriz de entrada exceto as duas primeiras linhas e colunas; ....
        maior_coluna(matriz, vetor_linha, k)
        escalonamento(matriz, k)
    return matriz


"Essa função "


def somatorio(matriz_l, vetor_c, i):
    soma = 0
    for a in range(i):
        soma += matriz_l[i][a]*vetor_c[a]
    return soma


"Essa função "


def cria_c(matriz, vetorB):
    vetorC[0] = vetorB[0]
    for i in range(1, tamanho):
        somatorio(matriz, vetorC, i)
        for j in range(i):
            vetorC[i] = vetorB[i] - somatorio(matriz, vetorC, i)
    return vetorC


"Essa função "


def somatorio2(matrizU, vetorS, i):
    soma = 0
    for a in range(i):
        soma += vetorS[tamanho-1-a]*matrizU[tamanho-1-i][tamanho-1-a]
    return soma/matrizU[tamanho-1-i][tamanho-1-i]


"Essa função fornece a solução do sistema."


def solucao(matriz, vetorC):
    vetorS[tamanho-1] = vetorC[tamanho-1]/matriz[tamanho-1][tamanho-1]
    for i in range(1, tamanho):
        somatorio2(matriz, vetorS, i)
        vetorS[tamanho-1-i] = (vetorC[tamanho-1-i]/matriz[tamanho-1-i][tamanho-1-i]) - (somatorio2(matriz, vetorS, i))
    return vetorS


"Essa função calcula numericamente o determinante da matriz de entrada."


def det_matriz(matriz):
    determinante = 1
    for k in range(len(matriz)):
        determinante *= ((-1)**1)*matriz[k][k]
    if determinante != 0:
        print("Sistema possui uma única solução \ne seu determinante é aproximadamente:", determinante)
    else:
        print("Sistema não possui uma única solução!")
        sys.exit()
    return determinante


def polar(vetor):
    for linha in range(len(vetor)):
        vetor[linha] = cmath.polar(vetor[linha])
    return vetor


def final():
    cria_matriz(tamanho, matriz)
    print("\n"+"Escreve o vetor B:")
    cria_vetor(tamanho, vetorB)
    print("\n")
    print("Matriz:")
    imprime_matriz(matriz)
    print("\n"+"Vetor B:")
    imprime_vetor(vetorB)
    print("\n")
    decomposicao_lu(matriz, vetorB)
    print("Matriz L e U:")
    imprime_matriz(matriz)
    print("\n")
    det_matriz(matriz)
    cria_c(matriz, vetorB)
    print("\n"+"A solução do sistema (o vetor S) é:")
    solucao(matriz, vetorC)
    imprime_vetor(vetorS)
    print('\nOu em coordenadas polares:')
    imprime_vetor(polar(vetorS))
    return None


final()

