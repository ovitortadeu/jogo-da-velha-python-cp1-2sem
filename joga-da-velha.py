
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
        linha = int(input('''
                ========================          
                Você quer colocar em qual linha? 
                Ex: 
                °_|¹_|²_
                ===========================
                Sua Reposta:
                '''))
        return linha
        
def leiaCoordenadaColuna():
        coluna = int(input('''
                ========================          
                Você quer colocar em qual coluna? 
                Ex: 
                °_|_|_
                ¹_|_|_
                ²_|_|_
                ===========================
                Sua Reposta: 
                '''))
        return coluna

def imprimePontuacao(pontuacao):
    print(f'''
               Pontuação
               =====================================================
                                {pontuacao} 
               =====================================================     
          ''')


def posicaoValida(linha,coluna, tabuleiro):
    if coluna <= 2 and linha <= 2 or coluna >= 0 and linha >=0:
        if tabuleiro[0][0] == '-' or tabuleiro[0][1] == '-' or tabuleiro[0][2] =='-' or tabuleiro[1][0] =='-' or tabuleiro[1][1] =='-' or tabuleiro[1][2] =='-' or tabuleiro[2][0] =='-' or tabuleiro[2][1] == '-' or tabuleiro[2][2] == '-':
            return True
    else:
        return False
   
def verificaVencedor(matriz):
    if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X":
        jogador = True
        return jogador
    elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
        jogador = True
        return jogador
    elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
        jogador = True
        return jogador  
    elif matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
        jogador = True
        return jogador  
    elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
        jogador = True
        return jogador
    elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
        jogador = True
        return jogador
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
        jogador = True
        return jogador
    elif matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
        jogador = True
        return jogador
    elif matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O":
        jogador = True
        return jogador
    elif matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O":
        jogador = True
        return jogador
    elif matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O":
        jogador = True
        return jogador  
    elif matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O":
        jogador = True
        return jogador  
    elif matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O":
        jogador = True
        return jogador
    elif matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
        jogador = True
        return jogador
    elif matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
        jogador = True
        return jogador
    elif matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
        jogador = True
        return jogador
    else:
        return False


def verificaVelha(vencedor):
    if vencedor == False:
        print("A partida deu empate")

'''
façam os modos jxj e jxm facil aqui
tudo apos isso e so o dificil
(tirar o comentario e colocar aqui, antes do modo dificil deixando claro)
'''


def modoDificil(tabuleiro):
    dif =  print ('''
                    =============================================
                    Bem vindo ao modo díficil, aqui é o
                    lugar que é impossivel ganhar, somente
                    empates e a vitória da máquina irão acontecer
                    ==============================================
                    Vamos começar!
                    Melhor de 3
                    ===============================================
                    ''')
    jog = print(f'''
                    ================================================
                    Você começa, e irá ser o X
                    ================================================
                            ''')
    
    
def jogar(coluna, linha, tabuleiro, posicao):
    while True:
        if posicao == True:
            tabuleiro[coluna][linha] = "X"
            break
        elif posicao == False:
            print('posição errada')
        
    
    
    
def jogadaMaquinaDificil(tabuleiro, posicaoValida,jogar):
    jogar = False
    if tabuleiro[1][1] == posicaoValida:
        jogar = True
    elif tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == posicaoValida:
        jogar = True
    elif tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == posicaoValida:
        jogar = True
    elif tabuleiro[2][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == posicaoValida:
        jogar = True
    elif tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == posicaoValida:
        jogar = True
    elif tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][0] == posicaoValida and tabuleiro[2][2] == posicaoValida:
        jogar = True
    elif tabuleiro[0][2] == posicaoValida and tabuleiro[2][0] == posicaoValida:
        jogar = True
    elif tabuleiro[0][1] == posicaoValida:
        jogar = True
    elif tabuleiro[1][0] == posicaoValida:
        jogar = True
    elif tabuleiro[1][2] == posicaoValida:
        jogar = True
    elif tabuleiro[2][1] == posicaoValida:
        jogar = True      
        
        
def main():
    matriz = inicializarTabuleiro()
    menu = imprimeMenuPrincipal()
    pontuacao = 0
    '''
    aqui voces definem o tipo q vcs estao fazendo
    sigam oq eu fiz no menu 3 que e o dificil
    praticamente nao escreve nada aqui, deve estar tudo feito nas funcoes
    '''
    if menu == 3:
        modoDificil(matriz)
        for jogo in range(0,3):
            linha = leiaCoordenadaLinha()
            coluna = leiaCoordenadaColuna()
            jogar(coluna, linha, matriz, posicaoValida(linha, coluna, matriz))
            imprimirTabuleiro(matriz)
        verificaVencedor(matriz)
        verificaVelha(verificaVencedor(matriz))
        if verificaVencedor(matriz) == True:
            pontuacao +=1
            print(f'{imprimePontuacao(pontuacao)}')


main()