
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
        

def leiaCordenadaLinha():
    while True:
        linha = int(input("Digite a linha que você quer jogar de 1 a 3: "))
        if linha > 3 or linha < 1:
            print('Escolha um número de 1 a 3')
        else: 
            return linha

def leiaCordenadaColuna():
    while True:
        coluna = int(input("Digite a coluna que você quer jogar de 1 a 3: "))
        if coluna > 3 or coluna < 1:
            print('Escolha um número de 1 a 3')
        else: 
          return coluna

def posicaoValida(leiaCordenadaLinha, leiaCordenadaColuna , inicializarTabuleiro):
    if inicializarTabuleiro[leiaCordenadaLinha][leiaCordenadaColuna] ==  "-":
       return True
   
def verificaVencedor(inicializarTabuleiro):
    placarJogador1 = 0
    placarJogador2 = 0
    if inicializarTabuleiro()[0][0] == "X" and inicializarTabuleiro()[0][1] == "X" and inicializarTabuleiro()[0][2] == "X":
        placarJogador1 += 1
    elif inicializarTabuleiro()[1][0] == "X" and inicializarTabuleiro()[1][1] == "X" and inicializarTabuleiro()[1][2] == "X":
        placarJogador1 += 1
    elif inicializarTabuleiro()[2][0] == "X" and inicializarTabuleiro()[2][1] == "X" and inicializarTabuleiro()[2][2] == "X":
        placarJogador1 += 1  
    elif inicializarTabuleiro()[0][0] == "X" and inicializarTabuleiro()[1][0] == "X" and inicializarTabuleiro()[2][0] == "X":
        placarJogador1 += 1  
    elif inicializarTabuleiro()[0][1] == "X" and inicializarTabuleiro()[1][1] == "X" and inicializarTabuleiro()[2][1] == "X":
        placarJogador1 += 1
    elif inicializarTabuleiro()[0][2] == "X" and inicializarTabuleiro()[1][2] == "X" and inicializarTabuleiro()[2][2] == "X":
        placarJogador1 += 1
    elif inicializarTabuleiro()[0][0] == "X" and inicializarTabuleiro()[1][1] == "X" and inicializarTabuleiro()[2][2] == "X":
        placarJogador1 += 1
    elif inicializarTabuleiro()[0][2] == "X" and inicializarTabuleiro()[1][1] == "X" and inicializarTabuleiro()[2][0] == "X":
        placarJogador1 += 1
    elif inicializarTabuleiro()[0][0] == "O" and inicializarTabuleiro()[0][1] == "O" and inicializarTabuleiro()[0][2] == "O":
        placarJogador2 += 1
    elif inicializarTabuleiro()[1][0] == "O" and inicializarTabuleiro()[1][1] == "O" and inicializarTabuleiro()[1][2] == "O":
        placarJogador2 += 1
    elif inicializarTabuleiro()[2][0] == "O" and inicializarTabuleiro()[2][1] == "O" and inicializarTabuleiro()[2][2] == "O":
        placarJogador2 += 1  
    elif inicializarTabuleiro()[0][0] == "O" and inicializarTabuleiro()[1][0] == "O" and inicializarTabuleiro()[2][0] == "O":
        placarJogador2 += 1  
    elif inicializarTabuleiro()[0][1] == "O" and inicializarTabuleiro()[1][1] == "O" and inicializarTabuleiro()[2][1] == "O":
        placarJogador2 += 1
    elif inicializarTabuleiro()[0][2] == "O" and inicializarTabuleiro()[1][2] == "O" and inicializarTabuleiro()[2][2] == "O":
        placarJogador2 += 1
    elif inicializarTabuleiro()[0][0] == "O" and inicializarTabuleiro()[1][1] == "O" and inicializarTabuleiro()[2][2] == "O":
        placarJogador2 += 1
    elif inicializarTabuleiro()[0][2] == "O" and inicializarTabuleiro()[1][1] == "O" and inicializarTabuleiro()[2][0] == "O":
        placarJogador2 += 1
    else:
        return False
        return True, placarJogador1, placarJogador2



def verificaVelha(VerificaVencedor):
    if VerificaVencedor == False:
        print("A partida deu empate")
    else:
        print("Alguma coisa deu errado ai irm")

verificaVelha(verificaVencedor)

#imprimeMenuPrincipal()
#matriz = inicializarTabuleiro()
#imprimirTabuleiro(matriz)