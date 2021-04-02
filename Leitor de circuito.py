"""A função conversor converte o arquivo txt (nome_arquivo) em uma matriz contendo as informações do circuito
(matriz) como segue:
    i) nó 'de';
    ii) nó 'para';
    iii) inicial do componente;
    iv) valor conforme o SI.
Ao final, deixe uma linha em branco."""


def conversor():
    nome_arquivo = input('Por favor, insira o nome do arquivo contendo as 4 informações acima e espaçadas por '
                         'espaço somente: ')  # Permite o usuário entrar com o nome do texto;
    conteudo = open(nome_arquivo, 'r', encoding='utf-8')  # Abre o arquivo;
    matriz = list()  # Declara a matriz que receberá as informações;
    for linha in conteudo:
        matriz.append([int(linha.split()[0]), int(linha.split()[1]),
                       str(linha.split()[2]), float(linha.split()[3])])  # Transforma cada linha do texto (conteudo) em
        # um vetor. Seus elementos são as 4 informações. Assim, por meio da iteração acima, realizada no vetor, adiciona
        # esses elementos na matriz (matriz).
    conteudo.close()  # Fecha o arquivo
    print(f'Circuito original: {matriz}')
    return matriz  # Retorna a matriz pronta para a realização de cálculos


"""A função circuitodc varre a matriz-circuito verificando a existência de capacitores e indutores. Por meio da teoria
de circuitos, ao considerar o ramo do capacitor como aberto e o ramo do indutor como curto-circuito, obtemos um circuito
DC. A próxima função realiza tal tarefa."""


def circuitodc(matriz):
    for linha in range(len(matriz)):  # Itera sobre a matriz em busca de capacitores (C) e indutores (L);
        if matriz[linha][2] == 'C':
            matriz[linha][2], matriz[linha][3] = 'R', 1e12  # Numericamente equivalente a um ramo aberto;
        elif matriz[linha][2] == 'L':
            matriz[linha][2], matriz[linha][3] = 'R', 1e-12  # Numericamente equivalente a um curto-circuito;
    print(f'Circuito DC: {matriz}')
    return matriz  # Após as alterações, a função retorna o circuito DC.


circuitodc(conversor())
