def countdown(n):
    """
    countdown takes an integer and prints out a countdown from n to 1

    >>> countdown(5)
    5
    4
    3
    2
    1
    >>> countdown(1)
    1
    >>> countdown(0)
    AssertionError: n must be an positive integer
    """

    assert n >= 1 and type(n) == int, "n must be an positive integer"
    if n == 1:
        print(n)
    else:
        print(n)
        return countdown(n - 1)

countdown(1)