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

from typing import Dict, Optional, Tuple

from .enums import Error, Flags, default_flags
from .error import IllegalNameError, RedifinitionError, UndefinedError
from .evaluate import evaluate
from .token import Function, Ref, Token


def verify_identifier(name: str) -> bool:
    return bool(
        name
        and not name[0].isdigit()
        and all(char.isascii() and (char.isalnum() or char == "_") for char in name)
    )


class Mathex:
    """Configuration for parsing."""

    def __init__(self, flags: Flags = default_flags):
        """Initializes a Mathex object with the specified evaluation flags.

        Args:
            flags (Flags, optional): Evaluation flags. Defaults to default_flags.
        """
        self._flags: Flags = flags
        self._tokens: Dict[str, Token] = {}

    def add_variable(self, name: str, variable: Ref):
        """Inserts a variable into the configuration object to be available for use in the expressions.

        Args:
            name (str): String representing name of the variable. (should only contain letters, digits or underscore and cannot start with a digit)
            variable (Ref): Reference to value of the variable. Lifetime of a reference is responsibility of a caller.

        Raises:
            IllegalNameError: Name contains illegal characters.
            RedifinitionError: Variable was already defined.
        """
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = Token.from_variable(variable)

    def add_constant(self, name: str, value: float):
        """Inserts a constant into the configuration object to be available for use in the expressions.

        Args:
            name (str): String representing name of the variable. (should only contain letters, digits or underscore and cannot start with a digit)
            value (float): Value of a constant variable.

        Raises:
            IllegalNameError: Name contains illegal characters.
            RedifinitionError: Variable was already defined.
        """
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = Token.from_constant(value)

    def add_function(self, name: str, function: Function):
        """Inserts a function into the configuration object to be available for use in the expressions.

        Args:
            name (str): String representing name of the function. (should only contain letters, digits or underscore and cannot start with a digit)
            function (Function): Function that takes list of arguments and returns tuple of result and None or tuple or None and error code.

        Raises:
            IllegalNameError: Name contains illegal characters.
            RedifinitionError: Function was already defined.
        """
        if not verify_identifier(name):
            raise IllegalNameError(name)

        if name in self._tokens:
            raise RedifinitionError(name, self._tokens[name])

        self._tokens[name] = Token.from_function(function)

    def remove(self, name: str):
        """Removes a variable or a function with given name that was added using `addVariable`, `addConstant` or `addFunction`.

        Args:
            name (str): String representing name of the variable or function to remove.

        Raises:
            UndefinedError: Variable or function with given name is not defined.
        """
        if name not in self._tokens:
            raise UndefinedError(name)

        del self._tokens[name]

    def evaluate(self, expression: str) -> Tuple[Optional[float], Optional[Error]]:
        """Takes mathematical expression and evaluates its numerical value.

        Args:
            expression (str): String to evaluate.

        Returns:
            Tuple[Optional[float], Optional[Error]]: Result or an error code.
        """
        return evaluate(expression, self._flags, self._tokens)
