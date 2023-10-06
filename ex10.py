N = int(input('Digite um tamanho para os vetores: '))
A = [0] * N
B = [0] * N
soma = [0] * N

for x in range(N):
    A[x] = int(input(f'Digite um número para a posição {x} do vetor A: '))
    B[x] = int(input(f'Digite um número para a posição {x} do vetor B: '))
    soma[x] = A[x] + B[x]

print(f'A: {A}\nB: {B}\nSoma: {soma}')