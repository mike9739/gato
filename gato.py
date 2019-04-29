#crea una lista con las posiciones para el tablero
board = [' ' for x in range(10)]
#funcionoara insetar un simbolo , recibe un simbolo X/O y una posicion POS
def insertLetter(letter, pos):
    board[pos] = letter
#verifica si el espacio esta libre
def spaceIsFree(pos):
    return board[pos] == ' '
#dibujar el tablero
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
 #verifica si hay un ganador   
def isWinner(bo, le):
    #sistemas de reglas :D
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Por favor seleccione la posicion donde quiera poner una \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('El lugar ya esta ocupado, por favor intente otra posicion!')
            else:
                print('Por favor seleccione un numero dentro del rango!')
        except:
            print('Por favor escriba un numero!')
            

def compMove():
    #genera una lista con los posibles movimientos
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    #Revisa si la maquina puede ganar o el jugafor va a ganar
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    #trata de tomar las esquinas
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    #trata de ganar el centro
    if 5 in possibleMoves:
        move = 5
        return move
    #trata de ganar los bordes
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move


    #selecciona una jugada aleatoriamente 
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def PVE():
    print('Vamos a jugar al gato :D')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('La computadora te gano :C')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Empate :/!')
            else:
                insertLetter('O', move)
                print('La compputadora coloco una O en:', move , ':')
                printBoard(board)
        else:
            print('Le ganastesss! :D')
            break

    if isBoardFull(board):
        print('Empate!')

def PCVSPC():
    print('disfruta dfel juego :D')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            move = compMove()
            if move == 0:
                print('Empate')
            else:
                insertLetter('X',move)
                print('La compputadora coloco una O en:', move , ':')
                printBoard(board)

        else:
            print('La computadora 2 gano')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Empate :/!')
            else:
                insertLetter('O', move)
                printBoard(board)
        else:
            print('PC1 gano')
            break

    if isBoardFull(board):
        print('Empate!')

while True:
    option = input('Quieres que juegue contra la PC(1) o contra ti (2)?')
    if option.lower() == '1':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        PCVSPC()
    else:
        answer = input('Quieres volver a jugar? (Y/N)')
        if answer.lower() == 'y' or answer.lower == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            PVE()
        else:
            break
