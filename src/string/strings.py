import re

class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """Verifica si una cadena es un palíndromo."""
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """Invierte una cadena sin usar slicing ni reversed()."""
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """Cuenta el número de vocales en una cadena."""
        vocales = "aeiouáéíóú"
        return sum(1 for c in texto.lower() if c in vocales)
    
    def contar_consonantes(self, texto):
        """Cuenta el número de consonantes en una cadena."""
        consonantes = "bcdfghjklmnñpqrstvwxyz"
        return sum(1 for c in texto.lower() if c in consonantes)
    
    def es_anagrama(self, texto1, texto2):
        """Verifica si dos cadenas son anagramas."""
        t1 = sorted(c.lower() for c in texto1 if c.isalnum())
        t2 = sorted(c.lower() for c in texto2 if c.isalnum())
        return t1 == t2
    
    def contar_palabras(self, texto):
        """Cuenta el número de palabras en una cadena."""
        return len([p for p in texto.split(" ") if p.strip() != ""])
    
    def palabras_mayus(self, texto):
        """Convierte en mayúscula la primera letra de cada palabra, manteniendo los espacios."""
        def capitalizar(match):
            palabra = match.group(0)
            return palabra.capitalize()
        return re.sub(r'\S+', capitalizar, texto)
    
    def eliminar_espacios_duplicados(self, texto):
        """Elimina espacios duplicados entre palabras, mantiene espacios al inicio y final."""
        return re.sub(r' {2,}', ' ', texto)
    
    def es_numero_entero(self, texto):
        """Verifica si una cadena representa un número entero."""
        if not texto:
            return False
        if texto[0] in ['-', '+']:
            return texto[1:].isdigit()
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        """Aplica el cifrado César a una cadena."""
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                nuevo = (ord(c) - base + desplazamiento) % 26 + base
                resultado += chr(nuevo)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """Descifra un texto cifrado con el método César."""
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """Encuentra todas las posiciones de una subcadena en un texto."""
        if not subcadena:
            return []
        posiciones = []
        n, m = len(texto), len(subcadena)
        for i in range(n - m + 1):
            if texto[i:i+m] == subcadena:
                posiciones.append(i)
        return posiciones
