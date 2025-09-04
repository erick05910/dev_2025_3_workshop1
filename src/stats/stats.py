class Stats:
    def promedio(self, numeros):
        """
        Calcula el promedio (media aritmética) de una lista de números.
        Retorna 0 si la lista está vacía.
        """
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Calcula la mediana de una lista de números.
        Retorna 0 si la lista está vacía.
        """
        if not numeros:
            return 0
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mitad = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:
            return numeros_ordenados[mitad]
    
    def moda(self, numeros):
        """
        Calcula la moda de una lista de números.
        Retorna None si la lista está vacía.
        En caso de empate, devuelve la primera moda encontrada.
        """
        if not numeros:
            return None
        frecuencias = {}
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        max_frecuencia = max(frecuencias.values())
        for num in numeros:
            if frecuencias[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar (poblacional) de una lista de números.
        Retorna 0 si la lista está vacía.
        """
        if not numeros:
            return 0
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):
        """
        Calcula la varianza (poblacional) de una lista de números.
        Retorna 0 si la lista está vacía.
        """
        if not numeros:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre máximo y mínimo) de una lista de números.
        Retorna 0 si la lista está vacía.
        """
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
