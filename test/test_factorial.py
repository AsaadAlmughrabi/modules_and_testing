from factorial_module.factorial_module import *

#test_factorial_iterative
def test_factorial1():
    actual = factorial_iterative(1)
    expected = 1
    assert actual == expected


def test_factorial2():
    actual = factorial_iterative(2)
    expected = 2
    assert actual == expected

#factorial_recursion
def test_factorial3():
    actual = factorial_iterative(3)
    expected = 6
    assert actual == expected


def test_factorial_recursion1():
    actual = factorial_recursive(1)
    expected = 1
    assert actual == expected


def test_factorial_recursion2():
    actual = factorial_recursive(2)
    expected = 2
    assert actual == expected


def test_factorial_recursion3():
    actual = factorial_recursive(3)
    expected = 6
    assert actual == expected

#test clumsy
def test_clumsy1():
    actual = clumsy(1)
    expected = 1
    assert actual == expected


def test_clumsy2():
    actual = clumsy(2)
    expected = 2
    assert actual == expected


def test_clumsy3():
    actual = clumsy(3)
    expected = 6
    assert actual == expected


def test_clumsy4():
    actual = clumsy(4)
    expected = 7
    assert actual == expected


def test_clumsy5():
    actual = clumsy(10)
    expected = 12
    assert actual == expected
