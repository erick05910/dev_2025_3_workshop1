class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        """Implementa la operación lógica AND."""
        return a and b
    
    def OR(self, a, b):
        """Implementa la operación lógica OR."""
        return a or b
    
    def NOT(self, a):
        """Implementa la operación lógica NOT."""
        return not a
    
    def XOR(self, a, b):
        """Implementa la operación lógica XOR (OR exclusivo)."""
        return (a and not b) or (not a and b)
    
    def NAND(self, a, b):
        """Implementa la operación lógica NAND (NOT AND)."""
        return not (a and b)
    
    def NOR(self, a, b):
        """Implementa la operación lógica NOR (NOT OR)."""
        return not (a or b)
    
    def XNOR(self, a, b):
        """Implementa la operación lógica XNOR (NOT XOR)."""
        return not ((a and not b) or (not a and b))
    
    def implicacion(self, a, b):
        """Implementa la operación lógica de implicación (a -> b)."""
        return (not a) or b
    
    def bi_implicacion(self, a, b):
        """Implementa la operación lógica de bi-implicación (a <-> b)."""
        return a == b
