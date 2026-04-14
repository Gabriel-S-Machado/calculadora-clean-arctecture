class ValorNumerico:
    """Representa um valor numérico válido no dominio."""
    def __init__(self, valor: float):
        if not isinstance(valor, float): raise TypeError("'ValorNumerico' deve ser 'float'!")
        self._value = valor

    def __repr__(self):
        return f"ValorNumerico({type(self._value)}({self._value}))"
    
    def __str__(self):
        return f"{self.value}"

    @property
    def como_float(self)-> float:
        """Retorna o valor contido no objeto como float."""
        return self._value
    
