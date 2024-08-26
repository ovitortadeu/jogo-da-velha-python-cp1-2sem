

def inicializarTabuleiro():
    velha = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
    return velha

def imprimirTabuleiro(velha):
    jogo_da_velha = (f'''
            {velha[0][0]}|{velha[0][1]}|{velha[0][2]}
            {velha[1][0]}|{velha[1][1]}|{velha[1][2]}
            {velha[2][0]}|{velha[2][1]}|{velha[2][2]}
                ''')
    print(jogo_da_velha)


def imprimeMenuPrincipal():
    while True:
        menu = int(input('''
            Bem vindo ao Jogo da velha
            ==========================
            Qual modo você gostaria de jogar?
            =================================
            1 - JxJ
            2 - JxM (fácil)
            3 - JxM (difícil)
            ==================================
            Sua resposta: '''))
        if menu > 3 or menu < 1:
            print('Escolha uma opção de 1 a 3 por favor')
        else:
            return menu
                







imprimeMenuPrincipal()
matriz = inicializarTabuleiro()
imprimirTabuleiro(matriz)
