from enum import Enum, auto
from typing import Callable, TypeAlias
from dataclasses import dataclass
from math import fmod
from mathex.enums import Error


Function: TypeAlias = Callable[[list[float]], tuple[float, Error]]
BinaryOperator: TypeAlias = Callable[[float, float], float]
UnaryOperator: TypeAlias = Callable[[float], float]


class Ref:
    def __init__(self, value: float):
        self._value = value

    def set(self, value: float):
        self._value = value

    def get(self) -> float:
        return self._value


class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    COMMA = auto()
    CONSTANT = auto()
    VARIABLE = auto()
    FUNCTION = auto()
    BI_OPERATOR = auto()
    UN_OPERATOR = auto()


@dataclass(kw_only=True)
class Token:
    type: TokenType


@dataclass(kw_only=True)
class ConstantToken(Token):
    type: TokenType = TokenType.CONSTANT
    value: float


@dataclass(kw_only=True)
class VariableToken(Token):
    type: TokenType = TokenType.VARIABLE
    variable: Ref


@dataclass(kw_only=True)
class FunctionToken(Token):
    type: TokenType = TokenType.FUNCTION
    function: Function


@dataclass(kw_only=True)
class BiOperatorToken(Token):
    type: TokenType = TokenType.BI_OPERATOR
    biop: BinaryOperator
    prec: int
    lassoc: bool


@dataclass(kw_only=True)
class UnOperatorToken(Token):
    type: TokenType = TokenType.UN_OPERATOR
    unop: UnaryOperator
