from ..DOMINIO.VALUE_OBJECTS.resultado_operacao import ResultadoOperacao

class Calculadora:
    def __init__(self, id_calc: str, /, ultimosResultados: list[ResultadoOperacao] = None, tamanhoHistorico: int | None = None):
        self._id_calc = id_calc
        self.ultimosResultados = ultimosResultados
        self.tamanhoHistorico = 10 if tamanhoHistorico is None else tamanhoHistorico

    def __repr__(self):
        return f"calculadora_{self._id_calc}"
    
    def __str__(self):
        return f"calculadora_{self._id_calc}"
    
    @property
    def id_calc(self):
        return self._id_calc
    
    def gravar_resultado(self, resultado: ResultadoOperacao):
        """Salva o resultado, substituindo os mais antigos pelos mais novos."""
        if not isinstance(resultado, ResultadoOperacao): 
            raise TypeError(f"'resultado' gravado não deve ser '{type(resultado)}'")

        if self.ultimosResultados is None: self.ultimosResultados = [resultado]
        elif len(self.ultimosResultados) >= self.tamanhoHistorico:
            self.ultimosResultados.pop(0)
            self.ultimosResultados.append(resultado)