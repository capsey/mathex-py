from mathex.token import Token, BiOperatorToken, UnOperatorToken
from math import fmod


def add_wrapper(a: float, b: float) -> float:
    return a + b


def sub_wrapper(a: float, b: float) -> float:
    return a - b


def mul_wrapper(a: float, b: float) -> float:
    return a * b


def div_wrapper(a: float, b: float) -> float:
    return a / b


def pos_wrapper(x: float) -> float:
    return x


def neg_wrapper(x: float) -> float:
    return -x


add_token: Token = BiOperatorToken(biop=add_wrapper, prec=2, lassoc=True)
sub_token: Token = BiOperatorToken(biop=sub_wrapper, prec=2, lassoc=True)
mul_token: Token = BiOperatorToken(biop=mul_wrapper, prec=3, lassoc=True)
div_token: Token = BiOperatorToken(biop=div_wrapper, prec=3, lassoc=True)

pow_token: Token = BiOperatorToken(biop=pow, prec=2, lassoc=True)
mod_token: Token = BiOperatorToken(biop=fmod, prec=2, lassoc=True)

pos_token: Token = UnOperatorToken(unop=pos_wrapper)
neg_token: Token = UnOperatorToken(unop=neg_wrapper)
