from functions import *

with open('teste5.txt', encoding='utf-8') as file:
    string = file.read()
    # print(string)

codification, tree = codificarhuffman(string)
print('')
# print(f'Saída codificada: {codificacao}')
# print(f'Saída decodificada: {decodificarhuffman(codificacao, arvore)}')

if string == decodificarhuffman(codification, tree):
    print('')
    print(True)
else:
    print(False)

