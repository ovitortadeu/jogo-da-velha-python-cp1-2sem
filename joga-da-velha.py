

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
                
def leiaCoordenadaLinha():
    while True:
        linha = int(input('''
                ========================          
                Você quer colocar em qual linha? 
                Ex: 
                ¹_|²_|³_
                ===========================
                Sua Reposta:
                '''))
        if linha > 3 or linha < 1:
            print('por favor tente coloque em uma posicao valida')
        else:
            return linha
        
def leiaCoordenadaColuna():
    while True:
        linha = int(input('''
                ========================          
                Você quer colocar em qual coluna? 
                Ex: 
                ¹_|_|_
                ²_|_|_
                ³_|_|_
                ===========================
                Sua Reposta: 
                '''))
        if linha > 3 or linha < 1:
            print('por favor tente coloque em uma posicao valida')
        else:
            return linha

def imprimePontuacao(jogador, pontuacao):
    print(f'''
               =====================================================
               O jogador {jogador} está com {pontuacao} pontos 
               =====================================================     
          ''')


def posicaoValida(tabuleiro):
    while True:
        if tabuleiro[0][0] == '-' or tabuleiro[0][1] == '-' or tabuleiro[0][2] =='-' or tabuleiro[1][0] =='-' or tabuleiro[1][1] =='-' or tabuleiro[1][2] =='-' or tabuleiro[2][0] =='-' or tabuleiro[2][1] =='-' or tabuleiro[2][2] == '-':
            return True
        else:
            print('Posição inválida')


def verificaVencedor(tabuleiro, linha, coluna):
    if linha.all('x') or linha.all('o'):
        return True
    elif coluna.all('x') or coluna.all('o'):
        return True
    elif tabuleiro[0][0] and tabuleiro[1][1] and tabuleiro[2][2] == 'x' or tabuleiro[0][2] and tabuleiro[1][1] and tabuleiro[2][0]:
        return True
        
    
        
    





# imprimeMenuPrincipal()
# leiaCoordenadaLinha()
# matriz = inicializarTabuleiro()
# imprimirTabuleiro(matriz)