# Representamos el tablero como una lista de listas 3x3
tablero = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# Función para imprimir el tablero de forma legible
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()

# Función que evalúa el estado actual del tablero
def evaluar(tablero):
    # Comprobamos si hay un ganador en las filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2]:
            if tablero[fila][0] == 'X':
                return 10
            elif tablero[fila][0] == 'O':
                return -10

    # Comprobamos si hay un ganador en las columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna]:
            if tablero[0][columna] == 'X':
                return 10
            elif tablero[0][columna] == 'O':
                return -10

    # Comprobamos si hay un ganador en las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        if tablero[0][0] == 'X':
            return 10
        elif tablero[0][0] == 'O':
            return -10

    if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        if tablero[0][2] == 'X':
            return 10
        elif tablero[0][2] == 'O':
            return -10

    # Si no hay ganador, devolvemos 0
    return 0

# Función para comprobar si hay un empate
def es_empate(tablero):
    for fila in tablero:
        if '' in fila:
            return False
    return True

# Algoritmo Minimax
def minimax(tablero, profundidad, esMax):
    puntuacion = evaluar(tablero)

    # Si alguien ha ganado, devolvemos el valor de la jugada
    if puntuacion == 10:
        return puntuacion
    if puntuacion == -10:
        return puntuacion
    if es_empate(tablero):
        return 0

    # Si es el turno de "Max" (jugador X)
    if esMax:
        mejor = -1000
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '':
                    tablero[i][j] = 'X'
                    mejor = max(mejor, minimax(tablero, profundidad + 1, False))
                    tablero[i][j] = ''
        return mejor

    # Si es el turno de "Min" (jugador O)
    else:
        mejor = 1000
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '':
                    tablero[i][j] = 'O'
                    mejor = min(mejor, minimax(tablero, profundidad + 1, True))
                    tablero[i][j] = ''
        return mejor

# Función para encontrar la mejor jugada para el jugador X
def mejor_jugada(tablero):
    mejor_valor = -1000
    mejor_movimiento = (-1, -1)

    # Recorremos todas las casillas
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == '':
                tablero[i][j] = 'X'
                movimiento_valor = minimax(tablero, 0, False)
                tablero[i][j] = ''

                if movimiento_valor > mejor_valor:
                    mejor_jugada = (i, j)
                    mejor_valor = movimiento_valor

    return mejor_jugada

# Ejemplo de uso
if __name__ == "__main__":
    # Tablero inicial vacío
    imprimir_tablero(tablero)

    # Jugamos por turnos, empezando por la IA (X)
    while True:
        # Jugador X (IA)
        print("Turno del jugador X (IA):")
        movimiento = mejor_jugada(tablero)
        tablero[movimiento[0]][movimiento[1]] = 'X'
        imprimir_tablero(tablero)

        # Comprobamos si hay un ganador o empate
        if evaluar(tablero) == 10:
            print("¡Jugador X (IA) gana!")
            break
        if es_empate(tablero):
            print("¡Es un empate!")
            break

        # Jugador O (humano)
        print("Turno del jugador O (Humano):")
        fila = int(input("Introduce la fila (0, 1, 2): "))
        columna = int(input("Introduce la columna (0, 1, 2): "))
        if tablero[fila][columna] == '':
            tablero[fila][columna] = 'O'
        else:
            print("Movimiento inválido. Intenta de nuevo.")
            continue

        imprimir_tablero(tablero)

        # Comprobamos si hay un ganador o empate
        if evaluar(tablero) == -10:
            print("¡Jugador O (Humano) gana!")
            break
        if es_empate(tablero):
            print("¡Es un empate!")
            break
