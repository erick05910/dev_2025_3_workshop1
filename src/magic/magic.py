class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """
    
    def fibonacci(self, n):
        """Calcula el n-ésimo número de la secuencia de Fibonacci."""
        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
    
    def secuencia_fibonacci(self, n):
        """Genera los primeros n números de la secuencia de Fibonacci."""
        if n <= 0:
            return []
        seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq[:n]
    
    def es_primo(self, n):
        """Verifica si un número es primo."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """Genera una lista de números primos hasta n."""
        return [i for i in range(2, n + 1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        """Verifica si un número es perfecto."""
        if n < 2:
            return False
        suma = sum(i for i in range(1, n) if n % i == 0)
        return suma == n
    
    def triangulo_pascal(self, filas):
        """Genera las primeras n filas del triángulo de Pascal."""
        if filas <= 0:
            return []
        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        """Calcula el factorial de un número."""
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        """Calcula el máximo común divisor de dos números."""
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        """Calcula el mínimo común múltiplo de dos números."""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """Calcula la suma de los dígitos de un número."""
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        """Verifica si un número es de Armstrong."""
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d)**potencia for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """Verifica si una matriz es un cuadrado mágico."""
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False  # no es cuadrada
        
        suma_ref = sum(matriz[0])
        
        # filas
        for fila in matriz:
            if sum(fila) != suma_ref:
                return False
        
        # columnas
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_ref:
                return False
        
        # diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_ref:
            return False
        
        # diagonal secundaria
        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_ref:
            return False
        
        return True
