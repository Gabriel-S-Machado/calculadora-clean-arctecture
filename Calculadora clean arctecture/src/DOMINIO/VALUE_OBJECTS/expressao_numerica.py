from .valor_numerico import ValorNumerico
from .operacao import Operacao

class ExpressaoNumerica:
    """Representa intenções de cálculo, simples ou complexos."""

    def __init__(self, a: ValorNumerico | "ExpressaoNumerica", b: ValorNumerico | "ExpressaoNumerica", operacao: Operacao):
        if not isinstance(a, (ValorNumerico, ExpressaoNumerica)) or not isinstance(b, (ValorNumerico, ExpressaoNumerica)):
            raise TypeError(f"'a' e 'b' em ExpressaoNumerica devem ser" \
                            "'ValorNumerico' ou 'ExpressaoNumerica'!")
        elif not isinstance(operacao, Operacao):
            raise TypeError("'operacao' deve ser 'Opercao'!")
        
        self._a = a
        self._b = b
        self._operacao = operacao

    def __repr__(self): 
        return f"ExpressaoNumerica({self._a}, {self._b}, {self._operacao})"
    
    def __str__(self):
        return f"{self._a} {self._operacao} {self._b}"
    
    @property
    def principal(self): return self._a

    @property
    def secundario(self): return self._b

    @property
    def operador(self): return self._operacao