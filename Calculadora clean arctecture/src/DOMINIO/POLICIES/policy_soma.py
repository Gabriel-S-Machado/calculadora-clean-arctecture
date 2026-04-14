"""Responsável pela Policy de Adição"""

from ..VALUE_OBJECTS.valor_numerico import ValorNumerico

def policy_soma(a: ValorNumerico, b: ValorNumerico)-> ValorNumerico:
    """
    Recebe dois 'ValorNumerico' e retorna o 'ValorNumerico' resultante da operação.
    """
    if not isinstance(a, ValorNumerico) or not isinstance(b, ValorNumerico):
        raise TypeError("'a' e 'b' passadas devem ser 'ValorNumerico'!")
    
    else: return ValorNumerico(a.como_float + b.como_float)