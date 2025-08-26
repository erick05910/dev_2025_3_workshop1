class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
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
        if not numeros:
            return None   # 👈 cambio aquí
        frecuencias = {}
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        max_frecuencia = max(frecuencias.values())
        for num in numeros:  # devuelve el primero en caso de empate
            if frecuencias[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):
        if not numeros:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
