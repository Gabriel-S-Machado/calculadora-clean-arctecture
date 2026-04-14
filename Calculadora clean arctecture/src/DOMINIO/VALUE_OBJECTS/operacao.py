"""AST (Abstract Syntax Tree) do Dominio"""

from enum import Enum

class Operacao(Enum):
    ADICAO = "+"
    SUBTRACAO = "-"
    MULTIPLICACAO = "*"
    DIVISAO = "/"
    EXPONENCIACAO = "^"
