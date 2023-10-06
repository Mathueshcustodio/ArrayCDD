'''Exercício 09
Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e
mostrando seu nome e a mensagem, loginefetuado com sucesso.'''
nomes = [0,0,0,0,0]
senhas = [0,0,0,0,0]

#Cadastra os usuários
for x in range(5):
    nomes[x] = input("Digite o nome do usuário = ")
    senhas[x] = input("Digite a senha do usuário = ")

#Login
tentativas_login = 0
while tentativas_login < 3:
    login_nome = input('Usuário =  ')
    for i in range(5):
        if nomes[i] == login_nome:
            tentativas_login = 3
            print('Usuário encontrado!')
            for j in range(3): # 3 Tentativas para digitar a senha
                login_senha = input('Senha = ')
                if senhas[i] == login_senha:
                    print('Login realizado, bem vindo {}'.format(login_nome))
                    break
                else:
                    print('Senha invalida!')
    if tentativas_login < 3:
        print('Usuário Invalido')
    tentativas_login += 1