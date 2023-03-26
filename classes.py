# Nós de uma Árvore de Huffman
class Nodes:

    def __init__(self, frequencia, simbolo, left=None, right=None):
        # Frequencia de determinado símbolo
        self.frequencia = frequencia

        # Símbolo em análise
        self.simbolo = simbolo

        # Nó a esquerda
        self.left = left

        # Nó a direita
        self.right = right

        # A direção da árvore (0 ou 1)
        self.code = ''
