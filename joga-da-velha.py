
def inicializarTabuleiro():
    velha = [[0,0,0]
            ,[0,0,0]
            ,[0,0,0]]
    return velha
       

def imprimirTabuleiro(inicializarTabuleiro):
    print(f'''
        {inicializarTabuleiro[0][0]}|{inicializarTabuleiro[0][1]}|{inicializarTabuleiro[0][2]}
        {inicializarTabuleiro[1][0]}|{inicializarTabuleiro[1][1]}|{inicializarTabuleiro[1][2]}
        {inicializarTabuleiro[2][0]}|{inicializarTabuleiro[2][1]}|{inicializarTabuleiro[2][2]}
        ''')
        
    



matriz = inicializarTabuleiro()
imprimirTabuleiro(inicializarTabuleiro)