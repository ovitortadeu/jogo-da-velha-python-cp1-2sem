import random
'''
FIAP
1TDSPH - 2° semestre de 2024
Prof. Fernando Almeida

CHECKPOINT1 2° semestre(CP4)

VITOR TADEU SOARES DE SOUSA RM: 559105
PEDRO PAULO BARRETTA RM: 556370
GIOVANNI DE SOUZA LIMA RM: 556536

'''







#Inicializa o tabuleiro, preparando ele para as jogadas.
def inicializarTabuleiro():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

#Imprime o tabuleiro na tela, incluindo suas alterações nas partidas.
def imprimirTabuleiro(tabuleiro):
    print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
    print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
    print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])

#Menu principal para selecionar o modo de jogo.
def imprimeMenuPrincipal():
    while True:
        menu = int(input('''
Bem-vindo ao Jogo da Velha
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

#Lê e valida as coordenadas de linha e coluna.
def leiaCoordenadaLinha():
    while True:
        linha = int(input('''
========================          
Você quer colocar em qual linha? 
Ex:          
¹_|_|_
²_|_|_
³_|_|_
===========================
Sua Resposta: '''))
        if 1 <= linha <= 3:
            return linha
        else:
            print("Linha inválida! Deve ser entre 1 e 3.")
def leiaCoordenadaColuna():
    while True:
        coluna = int(input('''
========================          
Você quer colocar em qual coluna? 
Ex: 
1 2 3
_|_|_
_|_|_
_|_|_
===========================
Sua Resposta: '''))
        if 1 <= coluna <= 3:
            return coluna
        else:
            print("Coluna inválida! Deve ser entre 1 e 3.")

#Verifica se a posição escolhida é válida.
def posicaoValida(tabuleiro, linha, coluna):
    if 1 <= linha <= 3 and 1 <= coluna <= 3:
        if tabuleiro[linha-1][coluna-1] == ' ':
            return True
        else:
            print("Posição ocupada! Tente novamente.")
            return False
    else:
        print("Coordenadas inválidas! Tente novamente.")
        return False

#posição valida para a maquina (sem o print de erro)
def posicaoValidaMaquina(tabuleiro, linha, coluna):
    if 1 <= linha <= 3 and 1 <= coluna <= 3:
        if tabuleiro[linha-1][coluna-1] == ' ':
            return True
        else:
            return False
    else:
        return False

#aplica a jogada da maquina
def jogarMaquina(tabuleiro, linha, coluna, jogador):
    if posicaoValidaMaquina(tabuleiro, linha, coluna):
        tabuleiro[linha-1][coluna-1] = jogador
        return True
    return False

#Recebe as coordenadas dos jogadores e aplica elas dentro do jogo.
def jogar(tabuleiro, linha, coluna, jogador):
    if posicaoValida(tabuleiro, linha, coluna):
        tabuleiro[linha-1][coluna-1] = jogador
        return True
    return False

def jogadaUsuario(tabuleiro, jogador):
    while True:
        linha = leiaCoordenadaLinha()
        coluna = leiaCoordenadaColuna()
        if jogar(tabuleiro, linha, coluna, jogador):
            break

#escolhe um numero aleatório para as jogadas da maquina (facil)
def jogadaMaquina(tabuleiro, jogador):
    while True:
        linha = random.randint(1, 3)
        coluna = random.randint(1, 3)
        if jogarMaquina(tabuleiro, linha, coluna, jogador):
            break

def jogadaMaquinaDificil(tabuleiro, jogador):
    if jogador == 'X':
        adversario = 'O'
    else:
        adversario = 'X'
        
    '''
    Se está parte do tabuleiro estiver vazio, ele irá colocar na horizontal e para a função
    '''
    if tabuleiro[0][0] == tabuleiro[0][1] == jogador and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return
    if tabuleiro[0][0] == tabuleiro[0][2] == jogador and tabuleiro[0][1] == ' ':
        tabuleiro[0][1] = jogador
        return
    if tabuleiro[0][1] == tabuleiro[0][2] == jogador and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return
    
    if tabuleiro[1][0] == tabuleiro[1][1] == jogador and tabuleiro[1][2] == ' ':
        tabuleiro[1][2] = jogadorx
        return
    if tabuleiro[1][0] == tabuleiro[1][2] == jogador and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[1][2] == jogador and tabuleiro[1][0] == ' ':
        tabuleiro[1][0] = jogador
        return

    if tabuleiro[2][0] == tabuleiro[2][1] == jogador and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return
    if tabuleiro[2][0] == tabuleiro[2][2] == jogador and tabuleiro[2][1] == ' ':
        tabuleiro[2][1] = jogador
        return
    if tabuleiro[2][1] == tabuleiro[2][2] == jogador and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return

    '''
    Se está linha da coluna estiver vazia, ele irá colocar lá e para a função
    '''
    if tabuleiro[0][0] == tabuleiro[1][0] == jogador and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return
    if tabuleiro[0][0] == tabuleiro[2][0] == jogador and tabuleiro[1][0] == ' ':
        tabuleiro[1][0] = jogador
        return
    if tabuleiro[1][0] == tabuleiro[2][0] == jogador and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return
    
    if tabuleiro[0][1] == tabuleiro[1][1] == jogador and tabuleiro[2][1] == ' ':
        tabuleiro[2][1] = jogador
        return
    if tabuleiro[0][1] == tabuleiro[2][1] == jogador and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[2][1] == jogador and tabuleiro[0][1] == ' ':
        tabuleiro[0][1] = jogador
        return

    if tabuleiro[0][2] == tabuleiro[1][2] == jogador and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return
    if tabuleiro[0][2] == tabuleiro[2][2] == jogador and tabuleiro[1][2] == ' ':
        tabuleiro[1][2] = jogador
        return
    if tabuleiro[1][2] == tabuleiro[2][2] == jogador and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return

    '''
    Se a máquina pode ganhar pelos cantos, ele colocará lá e para a função
    '''
    if tabuleiro[0][0] == tabuleiro[1][1] == jogador and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return
    if tabuleiro[0][0] == tabuleiro[2][2] == jogador and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[2][2] == jogador and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return

    if tabuleiro[0][2] == tabuleiro[1][1] == jogador and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return
    if tabuleiro[0][2] == tabuleiro[2][0] == jogador and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[2][0] == jogador and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return

    '''
    Se o usuário for ganhar, a máquina irá colocar no lugar e para a função
    '''
    if tabuleiro[0][0] == tabuleiro[0][1] == adversario and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return
    if tabuleiro[0][0] == tabuleiro[0][2] == adversario and tabuleiro[0][1] == ' ':
        tabuleiro[0][1] = jogador
        return
    if tabuleiro[0][1] == tabuleiro[0][2] == adversario and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return

    if tabuleiro[1][0] == tabuleiro[1][1] == adversario and tabuleiro[1][2] == ' ':
        tabuleiro[1][2] = jogador
        return
    if tabuleiro[1][0] == tabuleiro[1][2] == adversario and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[1][2] == adversario and tabuleiro[1][0] == ' ':
        tabuleiro[1][0] = jogador
        return

    if tabuleiro[2][0] == tabuleiro[2][1] == adversario and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return
    if tabuleiro[2][0] == tabuleiro[2][2] == adversario and tabuleiro[2][1] == ' ':
        tabuleiro[2][1] = jogador
        return
    if tabuleiro[2][1] == tabuleiro[2][2] == adversario and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return

    if tabuleiro[0][0] == tabuleiro[1][0] == adversario and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return
    if tabuleiro[0][0] == tabuleiro[2][0] == adversario and tabuleiro[1][0] == ' ':
        tabuleiro[1][0] = jogador
        return
    if tabuleiro[1][0] == tabuleiro[2][0] == adversario and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return

    if tabuleiro[0][1] == tabuleiro[1][1] == adversario and tabuleiro[2][1] == ' ':
        tabuleiro[2][1] = jogador
        return
    if tabuleiro[0][1] == tabuleiro[2][1] == adversario and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[2][1] == adversario and tabuleiro[0][1] == ' ':
        tabuleiro[0][1] = jogador
        return

    if tabuleiro[0][2] == tabuleiro[1][2] == adversario and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return
    if tabuleiro[0][2] == tabuleiro[2][2] == adversario and tabuleiro[1][2] == ' ':
        tabuleiro[1][2] = jogador
        return
    if tabuleiro[1][2] == tabuleiro[2][2] == adversario and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return

    if tabuleiro[0][0] == tabuleiro[1][1] == adversario and tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return
    if tabuleiro[0][0] == tabuleiro[2][2] == adversario and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[2][2] == adversario and tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return

    if tabuleiro[0][2] == tabuleiro[1][1] == adversario and tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return
    if tabuleiro[0][2] == tabuleiro[2][0] == adversario and tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return
    if tabuleiro[1][1] == tabuleiro[2][0] == adversario and tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return

    '''
    Tem preferência pelo centro, sendo a prioridade
    '''
    if tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = jogador
        return

    '''
    Escolhe os cantos se puder
    '''
    if tabuleiro[0][0] == ' ':
        tabuleiro[0][0] = jogador
        return
    if tabuleiro[0][2] == ' ':
        tabuleiro[0][2] = jogador
        return
    if tabuleiro[2][0] == ' ':
        tabuleiro[2][0] = jogador
        return
    if tabuleiro[2][2] == ' ':
        tabuleiro[2][2] = jogador
        return

    '''
    Escolhe as bordas, se os cantos não estiverem abertos
    '''
    if tabuleiro[0][1] == ' ':
        tabuleiro[0][1] = jogador
        return
    if tabuleiro[1][0] == ' ':
        tabuleiro[1][0] = jogador
        return
    if tabuleiro[1][2] == ' ':
        tabuleiro[1][2] = jogador
        return
    if tabuleiro[2][1] == ' ':
        tabuleiro[2][1] = jogador
        return
            
#Imprime o placar atual
def imprimePontuacao(pontuacao):
    print('========================')
    print(f"Placar Atual:")
    print(f"Jogador 1 (X): {pontuacao['X']} vitórias")
    print(f"Jogador 2 (O): {pontuacao['O']} vitórias")
    print('========================')

#Verifica se a ultima jogada feita resultou em um vencedor ou empate.
def verificaVencedor(tabuleiro, jogador):
    vitoria = [
        [tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]],
        [tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]],
        [tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]],
        [tabuleiro[0][0], tabuleiro[1][0], tabuleiro[2][0]],
        [tabuleiro[0][1], tabuleiro[1][1], tabuleiro[2][1]],
        [tabuleiro[0][2], tabuleiro[1][2], tabuleiro[2][2]],
        [tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]],
        [tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]],
    ]
    for condicao in vitoria:
        if condicao == [jogador, jogador, jogador]:
            return True
    return False

def verificaVelha(tabuleiro):
    for linha in tabuleiro:
        for espaco in linha:
            if espaco == ' ':
                return False
    return True

#Modo de jogo entre dois jogadores.
def modoJogador(pontuacao):
    print('''
=============================================
Bem-vindo ao modo contra jogador, aqui é o
lugar aonde você irá lutar contra outra
pessoa.
==============================================
Vamos começar!
===============================================
Jogador 1 começa, e irá ser o X
================================================
''')
    
    while True:
        tabuleiro = inicializarTabuleiro()
        jogador_atual = 'X'  
        
        while True:
            print(f"É a vez do jogador {jogador_atual}")
            jogadaUsuario(tabuleiro, jogador_atual)
            imprimirTabuleiro(tabuleiro)

            if verificaVencedor(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} Venceu!!")
                pontuacao[jogador_atual] += 1
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                break
            elif verificaVelha(tabuleiro):
                print("Empate!!")
                break

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        imprimePontuacao(pontuacao)
        
        repetir = input("Deseja jogar novamente? (s/n): ")
        if repetir != 's':
            break
        else:
            jogador_atual = 'O' if jogador_atual == 'X' and not verificaVencedor(tabuleiro, jogador_atual) else jogador_atual

#modo de JogadorXMaquina(facil)
def modoMaquinaFacil(pontuacao):
    print('''
=================================================
Este é o modo Jogador vs Maquina (modo fácil).
=================================================
Vamos começar!
=================================================
Primeiro você começará e depois a maquina.
=================================================
          ''')
    while True:
        tabuleiro = inicializarTabuleiro()
        jogador_atual = 'X'
    
        while True:
            print(f'É a vez do jogador {jogador_atual}')
            if jogador_atual == 'X':
                jogadaUsuario(tabuleiro, jogador_atual)
            else:
                jogadaMaquina(tabuleiro, jogador_atual)
            imprimirTabuleiro(tabuleiro)
            if verificaVencedor(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} Venceu!!")
                pontuacao[jogador_atual] += 1
                break
            elif verificaVelha(tabuleiro):
                print("Empate!!")
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                break

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        imprimePontuacao(pontuacao)

        repetir = input("Deseja jogar novamente? (s/n): ")
        if repetir != 's':
            break
        else:
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def modoDificil(pontuacao):
    print('''
=============================================
Bem-vindo ao modo díficil, aqui é o
lugar que é impossível ganhar, somente
empates e a vitória da máquina irão acontecer
==============================================
Vamos começar!
================================================
Você começa, e irá ser o X
================================================
''')
    
    while True:
        tabuleiro = inicializarTabuleiro()
        jogador_atual = 'X'

        while True:
            if jogador_atual == 'X':
                print(f"É a vez do jogador {jogador_atual}")
                jogadaUsuario(tabuleiro, jogador_atual)
            else:
                print(f"É a vez da máquina ({jogador_atual})")
                jogadaMaquinaDificil(tabuleiro, jogador_atual)

            imprimirTabuleiro(tabuleiro)

            if verificaVencedor(tabuleiro, jogador_atual):
                print(f'{jogador_atual} venceu!')
                pontuacao[jogador_atual] += 1
                break
            elif verificaVelha(tabuleiro):
                print('Empate!')
                break

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        imprimePontuacao(pontuacao)
        
        repetir = input("Deseja jogar novamente? (s/n): ")
        if repetir != 's':
            break

#função principal
def main():
    pontuacao = {'X': 0, 'O': 0}
    menu = imprimeMenuPrincipal()
    if menu == 1: 
        modoJogador(pontuacao)
    if menu == 2:
        modoMaquinaFacil(pontuacao)
    if menu ==3:
        modoDificil(pontuacao)

main()