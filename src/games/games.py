import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        # Normalizar a minúsculas
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }
        
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
        # filas y columnas
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] not in (" ", ""):
                return tablero[i][0]
            if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] not in (" ", ""):
                return tablero[0][i]

        # diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] not in (" ", ""):
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] not in (" ", ""):
            return tablero[0][2]

        # empate o continua
        for fila in tablero:
            if " " in fila or "" in fila:
                return "continua"
        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        # No se puede quedar en el mismo lugar
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # Movimiento no recto
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Movimiento horizontal
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False

        # Movimiento vertical
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if tablero[f][desde_col] != " ":
                    return False

        return True
