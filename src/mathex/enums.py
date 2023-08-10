from enum import Flag, Enum, auto


class Flags(Flag):
    IMPLICIT_PARENTHESES = auto()
    IMPLICIT_MULTIPLICATION = auto()
    SCIENTIFIC_NOTATION = auto()
    ADDITION = auto()
    SUBSTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
    EXPONENTIATION = auto()
    MODULUS = auto()
    IDENTITY = auto()
    NEGATION = auto()


default_flags = (
    Flags.IMPLICIT_PARENTHESES
    | Flags.IMPLICIT_MULTIPLICATION
    | Flags.SCIENTIFIC_NOTATION
    | Flags.ADDITION
    | Flags.SUBSTRACTION
    | Flags.MULTIPLICATION
    | Flags.DIVISION
    | Flags.IDENTITY
    | Flags.NEGATION
)


class Error(Enum):
    DIVISION_BY_ZERO = auto()
    SYNTAX_ERROR = auto()
    UNDEFINED = auto()
    INVALID_ARGS = auto()
    INCORRECT_ARGS_NUM = auto()


class States(Enum):
    INTEGER_PART = auto()
    FRACTION_PART = auto()
    EXP_START = auto()
    EXP_VALUE = auto()
