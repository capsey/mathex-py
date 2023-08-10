from mathex import (
    Mathex,
    Ref,
    Error,
    IllegalNameError,
    RedifinitionError,
    UndefinedError,
)
from pytest import fixture, approx, raises


@fixture
def config() -> Mathex:
    config = Mathex()
    return config


def test_add_variable(config):
    x: Ref = Ref(5)
    y: Ref = Ref(3)

    config.add_variable("x", x)
    config.add_variable("y", y)

    with raises(RedifinitionError):
        config.add_variable("y", None)

    with raises(IllegalNameError):
        config.add_variable("رطانة", None)

    result, error = config.evaluate("x + y")
    assert not error and result == approx(8)

    x.set(3)
    y.set(10)

    result, error = config.evaluate("x + y")
    assert not error and result == approx(13)

    config.remove("x")
    config.remove("y")

    with raises(UndefinedError):
        config.remove("رطانة")

    _, error = config.evaluate("x + y")
    assert error == Error.UNDEFINED


def test_add_constant(config):
    config.add_constant("e", 2.71)
    config.add_constant("pi", 3.14)

    with raises(RedifinitionError):
        config.add_constant("pi", None)

    with raises(IllegalNameError):
        config.add_constant("رطانة", None)

    result, error = config.evaluate("e + pi")
    assert not error and result == approx(5.85)

    config.remove("e")
    config.remove("pi")

    with raises(UndefinedError):
        config.remove("رطانة")

    _, error = config.evaluate("e + pi")
    assert error == Error.UNDEFINED


def test_add_function(config):
    def foo_wrapper(args: list[float]) -> tuple[float, Error]:
        if len(args) != 0:
            return Error.INCORRECT_ARGS_NUM

        return -1.25, None

    def abs_wrapper(args: list[float]) -> tuple[float, Error]:
        if len(args) != 1:
            return Error.INCORRECT_ARGS_NUM

        return abs(args[0]), None

    config.add_function("foo", foo_wrapper)
    config.add_function("abs", abs_wrapper)

    with raises(RedifinitionError):
        config.add_function("abs", None)

    with raises(IllegalNameError):
        config.add_function("رطانة", None)

    result, error = config.evaluate("abs(foo()) + 1.12")
    assert not error and result == approx(2.37)

    config.remove("foo")
    config.remove("abs")

    with raises(UndefinedError):
        config.remove("رطانة")

    _, error = config.evaluate("abs(foo()) + 1.12")
    assert error == Error.UNDEFINED
