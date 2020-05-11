juego = [
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
]


'''def game_board(mapa, player=0, fila=0, col=0, display=False):
    try:
        print("   0  1  2")
        if not display:
            mapa[fila][columna]=player
        for count, fila in enumerate(mapa):
            print(count, fila)
        return mapa
    except IndexError as e:
        print("Asegurate de ingresar valores entre 0 y 2 en fila y columna.", e)
    except Exception as e:
        print("BAARRDDDEASTE")
        '''

# Condicion horizontal


def win(partida):
    for fila in juego:
        print(fila)
        if fila.count(fila[0]) == len(fila) and fila[0] != 0:
            print(f"El jugador {fila[0]} es el ganador horizontalmente!")

        # Condicion Vertical

    for col in range(len(juego)):
        check = []

        for fila in juego:
            check.append(fila[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"El jugador {fila[0]} es el ganador verticalmente!")

    # Condicion diagonal

    diag = []
    for ind in range(len(juego)):
        diag.append(juego[ind][ind])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"El jugador {diag[0]} es el ganador diagonalmente!")

    diag = []
    for co, fi in enumerate(reversed(range(len(juego)))):
        diag.append(juego[co][fi])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print(f"El jugador {fila[0]} es el ganador diagonalmente!")


def game_board(mapa, player=0, fila=0, col=0, display=False):
    try:
        print("   0  1  2")
        if not display:
            mapa[fila][columna] = player
        for count, fila in enumerate(mapa):
            print(count, fila)
        return mapa
    except IndexError as e:
        print("Asegurate de ingresar valores entre 0 y 2 en fila y columna.", e)
    except Exception as e:
        print("BAARRDDDEASTE")


jugando = True
players = [1, 2]
while play:
    juego = [
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2]]
    
    fin_juego=False
    juego=game_board(juego, display=True)
    while not fin_juego:
        jugador_actual=1
        col_elegida=int(input("Ingrese la columna que queres jugar (0, 1, 2): "))
        fila_elegida=int(input("Ingrese la fila que queres jugar (0, 1, 2): "))
        juego=game_board(juego, jugador_actual, col_elegida, fila_elegida)

#juego=game_board(juego, display=True)
#juego=game_board(juego, player=1, fila=1, columna=1)
