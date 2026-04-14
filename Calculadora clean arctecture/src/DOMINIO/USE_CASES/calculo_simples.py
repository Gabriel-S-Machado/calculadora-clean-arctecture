"""Utilizado para cálculos simples com dois elementos e uma única operação"""

import logging
from ...ENTITIES.calculadora import Calculadora
from ..VALUE_OBJECTS.expressao_numerica import ExpressaoNumerica
from ..VALUE_OBJECTS.operacao import Operacao
from ..POLICIES import policy_soma, policy_subtracao, policy_multiplicacao
from ..VALUE_OBJECTS.resultado_operacao import ResultadoOperacao

def main(calculadora: Calculadora, expressao_numerica: ExpressaoNumerica, *, logger: logging.logger):
    """Utilizado para cálculos simples com dois elementos e uma única operação"""

    if not isinstance(calculadora, Calculadora):
        raise ValueError(f"'{calculadora}' deve ser uma 'Calculadora', não '{type(calculadora)}'")
    
    if not isinstance(expressao_numerica, ExpressaoNumerica):
        raise ValueError(f"'{expressao_numerica}' deve ser uma 'ExpressaoNumerica', não '{type(expressao_numerica)}'")

    a = expressao_numerica.principal
    b = expressao_numerica.secundario

    

    match expressao_numerica.operador:
        case Operacao.ADICAO:
            resultado = policy_soma.policy_soma(a, b)

        case Operacao.SUBTRACAO:
            resultado = policy_subtracao.policy_subtracao(a, b)

        case Operacao.MULTIPLICACAO:
            resultado = policy_multiplicacao.policy_multiplicacao(a, b)

        case _: raise ValueError(f"Operação '{expressao_numerica.operador}' não suportada!")

    return ResultadoOperacao(resultado, expressao_numerica)

    ...