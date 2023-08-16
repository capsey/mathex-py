# Copyright (c) 2023 Caps Lock

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from enum import Enum, Flag, auto


class Flags(Flag):
    """Evaluation parameters."""

    IMPLICIT_PARENTHESES = auto()
    """Enable implicit parentheses."""
    IMPLICIT_MULTIPLICATION = auto()
    """Enable implicit multiplication."""
    SCIENTIFIC_NOTATION = auto()
    """Enable numbers in scientific notation."""
    ADDITION = auto()
    """Enable addition operator."""
    SUBSTRACTION = auto()
    """Enable substraction operator."""
    MULTIPLICATION = auto()
    """Enable multiplication operator."""
    DIVISION = auto()
    """Enable division operator."""
    EXPONENTIATION = auto()
    """Enable exponentiation operator."""
    MODULUS = auto()
    """Enable modulus operator."""
    IDENTITY = auto()
    """Enable unary identity operator."""
    NEGATION = auto()
    """Enable unary negation operator."""


default_flags: Flags = (
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
"""Default parameters. Does not include exponentiation and modulus operators."""


class Error(Enum):
    """Error codes."""

    DIVISION_BY_ZERO = auto()
    """Division by zero."""
    SYNTAX_ERROR = auto()
    """Expression syntax is invalid."""
    UNDEFINED = auto()
    """Function or variable name not found."""
    INVALID_ARGS = auto()
    """Arguments validation failed."""
    INCORRECT_ARGS_NUM = auto()
    """Incorrect number of arguments."""


class NumParts(Enum):
    INTEGER_PART = auto()
    FRACTION_PART = auto()
    EXP_START = auto()
    EXP_VALUE = auto()
