import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        if jugador1 not in reglas or jugador2 not in reglas:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"
        elif reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        vacios = {' ', ''}

        for fila in tablero:
            if fila[0] not in vacios and fila[0] == fila[1] == fila[2]:
                return fila[0]

        for col in range(3):
            if tablero[0][col] not in vacios and tablero[0][col] == tablero[1][col] == tablero[2][col]:
                return tablero[0][col]

        if tablero[0][0] not in vacios and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]
        if tablero[0][2] not in vacios and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        for fila in tablero:
            for celda in fila:
                if celda in vacios:
                    return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        n = len(tablero)

        if not (0 <= desde_fila < n and 0 <= desde_col < n and 0 <= hasta_fila < n and 0 <= hasta_col < n):
            return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if str(tablero[desde_fila][c]).strip() not in {"", " "}:
                    return False
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if str(tablero[f][desde_col]).strip() not in {"", " "}:
                    return False

        return True
