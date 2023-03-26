from classes import Nodes


def calculafrequencia(string):
    """Uma função auxiliar com a finalidade de calcular a frequência dos símbolos em um texto específico"""
    simbolos = dict()
    for item in string:
        if simbolos.get(item) is None:
            simbolos[item] = 1
        else:
            simbolos[item] += 1
    return simbolos


codigos = {}


def calculacodigo(node, value=''):
    """Uma função auxilar com a finalidade de calcular os códigos dos simbolos a partir da busca na árvore de Huffman"""
    # Código de Huffman para o nó atual
    new_value = value + str(node.code)

    if (node.left):
        calculacodigo(node.left, new_value)
    if (node.right):
        calculacodigo(node.right, new_value)

    if (not node.left and not node.right):
        codigos[node.simbolo] = new_value

    return codigos


def codificarsaida(string, codificacao):
    """Uma função auxiliar com a finalidade de fornecer o texto de entrada codificado"""
    saida_codificada = []
    for elemento in string:
        #print(codificacao[elemento], end='')
        saida_codificada.append(codificacao[elemento])

    string_codificada = ''.join([str(item) for item in saida_codificada])
    return string_codificada


def calculaganho(string, codificacao):
    """Uma função auxiliar com a finalidade de calcula a diferença entre os dados compactados e não-compactados"""
    # Quantidade total de bits para armazenar os dados antes da compressão
    antes_compressao = len(string)*8
    depois_compressao = 0
    simbolos = codificacao.keys()
    for simbolo in simbolos:
        contador = string.count(simbolo)
        # Cálculo de quantos bits são necessários para o simbolo no total
        depois_compressao += contador * len(codificacao[simbolo])

    print(
        f'Alocação de memória antes da compressão (em bits): {antes_compressao}')
    print(
        f'Alocação de memória depois da compressão (em bits): {depois_compressao}')
    print(
        f'A taxa de compressão foi de {(antes_compressao-depois_compressao)/antes_compressao:.1%}')


def codificarhuffman(string):
    """Função Principal que aplica a codificação de Huffman no conjunto de dados"""
    simbolo_freq = calculafrequencia(string)
    simbolos = simbolo_freq.keys()
    frequencias = simbolo_freq.values()
    print(f'Símbolos: {simbolos}')
    print(f'Frequências: {frequencias}')

    nos_arvore = []

    # Conversão dos símbolos e frequências em nós na árvore de huffman
    for simbolo in simbolos:
        nos_arvore.append(Nodes(simbolo_freq.get(simbolo), simbolo))

    while len(nos_arvore) > 1:
        # Organização de todos os nós baseado nas suas frequências
        nos_arvore = sorted(nos_arvore, key=lambda x: x.frequencia)

        # Pegando os dois menores nós
        right = nos_arvore[0]
        left = nos_arvore[1]

        left.code = 0
        right.code = 1

        # Combinando os 2 menores nós para criar um novo nó
        novo_no = Nodes((left.frequencia + right.frequencia),
                        (left.simbolo + right.simbolo), left, right)

        nos_arvore.remove(left)
        nos_arvore.remove(right)
        nos_arvore.append(novo_no)

    codificacao_huffman = calculacodigo(nos_arvore[0])
    print(f'Simbolos com códigos: {codificacao_huffman}')
    calculaganho(string, codificacao_huffman)
    saida_codificada = codificarsaida(string, codificacao_huffman)
    return saida_codificada, nos_arvore[0]


def decodificarhuffman(dado_codificado, arvore_huffman):
    raiz = arvore_huffman
    saida_decodificada = []

    for x in dado_codificado:
        if x == '1':
            arvore_huffman = arvore_huffman.right
        elif x == '0':
            arvore_huffman = arvore_huffman.left

        try:
            if arvore_huffman.left.simbolo is None and arvore_huffman.right.simbolo is None:
                pass
        except AttributeError:
            saida_decodificada.append(arvore_huffman.simbolo)
            arvore_huffman = raiz

    string = ''.join([str(item) for item in saida_decodificada])
    return string
