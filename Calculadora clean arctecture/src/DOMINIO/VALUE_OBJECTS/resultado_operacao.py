from .expressao_numerica import ExpressaoNumerica
from .valor_numerico import ValorNumerico

class ResultadoOperacao:
    """
    Representa resultados de operações no sistema, podendo conter seus cálculos.
    """

    def __init__(self, resultado: ValorNumerico, calculo: ExpressaoNumerica | None = None):
        if not isinstance(resultado, ValorNumerico):
            raise TypeError("'resultado' deve ser 'ValorNumerico'!")
        elif not isinstance(calculo, (ExpressaoNumerica, None)):
            raise TypeError("'calculo' deve ser 'ExpressaoNumerica' ou 'None'!")

        self._resultado = resultado
        self._calculo = calculo

    def __repr__(self):
        return f"ResultadoOperacao({self._resultado}, {self._calculo})"
    
    def __str__(self):
        return f"{self._resultado} ({self._calculo})"
    
    @property
    def resultado(self): return self._resultado

    @property
    def calculo(self): return self._calculo

    