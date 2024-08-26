

def inicializarTabuleiro():
    velha = [[0,0,0]
            ,[0,0,0]
            ,[0,0,0]]
    return velha
       

def imprimirTabuleiro(velha):
    tabuleiro = (f'''
            {velha()[0][0]}|{velha()[0][1]}|{velha()[0][2]}
            {velha()[1][0]}|{velha()[1][1]}|{velha()[1][2]}
            {velha()[2][0]}|{velha()[2][1]}|{velha()[2][2]}
                ''')
    print(tabuleiro)


imprimirTabuleiro(inicializarTabuleiro)