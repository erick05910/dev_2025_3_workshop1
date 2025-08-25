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

        # Validar entradas
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
        """
        Devuelve:
            "X" si gana X
            "O" si gana O
            "empate" si tablero lleno sin ganador
            "continua" si aún hay casillas vacías y no hay ganador

        Nota: Solo cuentan como marcas válidas "X" y "O" (mayúsculas).
              Cualquier otro valor (None, "", " ", "x", "o", 0, etc.) se toma como vacío.
        """
        VAL = {"X", "O"}

        def mark(celda):
            # Normaliza: solo "X" u "O" exactas cuentan
            if isinstance(celda, str):
                s = celda.strip()
                return s if s in VAL else ""
            return ""

        # Revisar filas
        for r in range(3):
            a, b, c = mark(tablero[r][0]), mark(tablero[r][1]), mark(tablero[r][2])
            if a and a == b == c:
                return a

        # Revisar columnas
        for col in range(3):
            a, b, c = mark(tablero[0][col]), mark(tablero[1][col]), mark(tablero[2][col])
            if a and a == b == c:
                return a

        # Revisar diagonales
        a, b, c = mark(tablero[0][0]), mark(tablero[1][1]), mark(tablero[2][2])
        if a and a == b == c:
            return a
        a, b, c = mark(tablero[0][2]), mark(tablero[1][1]), mark(tablero[2][0])
        if a and a == b == c:
            return a

        # ¿Hay casillas vacías?
        for fila in tablero:
            for celda in fila:
                if mark(celda) == "":
                    return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        n = len(tablero)  # tamaño del tablero (normalmente 8)

        # Validar dentro de límites
        if not (0 <= desde_fila < n and 0 <= desde_col < n and 0 <= hasta_fila < n and 0 <= hasta_col < n):
            return False

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
                if str(tablero[desde_fila][c]).strip() != "":
                    return False
        else:
            # Movimiento vertical
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if str(tablero[f][desde_col]).strip() != "":
                    return False

        return True
