class Stats:
    def promedio(self, numeros):
        """Calcula la media aritmética de una lista de números."""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """Encuentra el valor mediano de una lista de números."""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mitad = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:
            return numeros_ordenados[mitad]
    
    def moda(self, numeros):
        """Encuentra el valor que aparece con mayor frecuencia en la lista."""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        frecuencias = {}
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        max_frecuencia = max(frecuencias.values())
        for num in numeros:  # devuelve el primero en caso de empate
            if frecuencias[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        """Calcula la desviación estándar (poblacional)."""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):
        """Calcula la varianza (poblacional)."""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        """Calcula el rango (max - min)."""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        return max(numeros) - min(numeros)
