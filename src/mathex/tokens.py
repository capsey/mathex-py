from mathex.token import Token, BiOperatorToken, UnOperatorToken
from math import fmod

add_token: Token = BiOperatorToken(biop=lambda a, b: a + b, prec=2, lassoc=True)
sub_token: Token = BiOperatorToken(biop=lambda a, b: a - b, prec=2, lassoc=True)
mul_token: Token = BiOperatorToken(biop=lambda a, b: a * b, prec=3, lassoc=True)
div_token: Token = BiOperatorToken(biop=lambda a, b: a / b, prec=3, lassoc=True)

pow_token: Token = BiOperatorToken(biop=pow, prec=2, lassoc=True)
mod_token: Token = BiOperatorToken(biop=fmod, prec=2, lassoc=True)

pos_token: Token = UnOperatorToken(unop=lambda x: x)
neg_token: Token = UnOperatorToken(unop=lambda x: -x)
