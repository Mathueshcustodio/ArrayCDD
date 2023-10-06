'''Exercício 11
Faça um código para ler um vetor de 30 números. Após isto, ler mais um número
qualquer, calcular e escrever quantas vezes esse número aparece no vetor.
'''

numeros = [0] * 30
for x in range(30):
    numeros[x] = int(input('Digite um número: '))

qtd = 0
num = int(input('Digite o número a ser pesquisado: '))
for y in range(30):
    if num == numeros[y]:
        qtd += 1
print('O número {} aparece {} vezes na lista'.format(num, qtd))
