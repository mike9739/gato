import random

tablero = ['' for x in range(10)]
#funcion para posicionar piezas
def colocarPieza(pieza,posicion):
    tablero[posicion] = pieza
#verifica si la posicion donde se va a colocar la pieza esta libre o no
def espacioLibre(posicion):
    return tablero(posicion) == ' '

def dibujarTablero(tablero):
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
#verifica si existe un gandor, revisa todas las posibles condiciones de victoria, recibe dos parametros
#un tablero y una pieza
def ganador(tablero,pieza):
    return(tablero[7]==pieza and tablero[8] and tablero[9])or(tablero[4]==pieza and tablero[5] and tablero[6])or(tablero[1]==pieza and tablero[2] and tablero[3])or  (tablero[1]==pieza and tablero[4] and tablero[7])or  (tablero[2]==pieza and tablero[5] and tablero[8])or (tablero[3]==pieza and tablero[6] and tablero[9])or (tablero[1]==pieza and tablero[5] and tablero[9])or (tablero[7]==pieza and tablero[5] and tablero[3]) 

def jugadaHumana():
    run = True
    while run:
        jugada = input('Por favor , selecciona el lugar donde quieres poner tu \'X\' (1-9)')
        ##verifica que el jugador inserte un valor valido
        try:
            jugada = int(jugada)
            if jugada > 0 and jugada < 10:
                if espacioLibre(jugada):
                    run = False
                    colocarPieza('X',jugada)
                else:
                    print('El espacio esta ocupado')
            else:
                print('Por favor ingresa un numero dentro del rango! (1-9):  ')

        except:
            print('por favor ingresa un numero!!')

def jugadaPC():
    judasPosibles = [x for x, pieza in enumerate(tablero) if pieza == '' and x != 0]
    jugada = 0

    for let in['O','X']:
        for i in judasPosibles:
            tablerocopia = tablero[:] #hace una copia del tablero
            tablerocopia[i] = let
            if ganador(tablerocopia,let):
                jugada = i
                return jugada
    
    esquinasAbiertas = []
    for i in judasPosibles:
        if i in [1,3,7,9]:
            esquinasAbiertas.append(i)
    if len(esquinasAbiertas)>0:
        jugada = seleccionAleatoria(esquinasAbiertas)
        return jugada
    if 5 in judasPosibles:
        jugada = 5
        return judasPosibles    
    bordesAbiertos = []
    for i in judasPosibles:
        if i in [2,4,6,8]:
             bordesAbiertos.append(i)
    if len( bordesAbiertos)>0:
        jugada = seleccionAleatoria( bordesAbiertos)
    return jugada




def seleccionAleatoria(lista):
    ln = len(lista)
    r = random.randrange(0,ln)
    return lista[r]

    
#cuenta el numero de espacios vacios que quedan
def tableroLleno(tablero):
    if tablero.count(' ')>1:
        return False
    else:
        return True


print('juguemos al gato :3')
dibujarTablero(tablero)
##mientras el tablero no esta lleno se sigue ejecuntando el juego
while not(tableroLleno(tablero)):
    if  not(ganador(tablero,'O')):
        jugadaHumana()
        dibujarTablero(tablero)
    else:
        print('La PC te gano :v')
        break
    if  not(ganador(tablero,'X')):
        jugada = jugadaPC()
        if jugada == 0:
            print('EMPATE XD!')
        else:
            colocarPieza('O',tablero)
            print('Tu pc coloco \'O\' in posicion',jugada,':')
            dibujarTablero(tablero)

    else:
        print('hay le  ganastesss :D')
        break
if tableroLleno(tablero):
    print('EMPATE XD')




