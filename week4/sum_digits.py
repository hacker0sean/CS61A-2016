def sum_digits(n):
    """
    sum_digits sums the digits of number n

    >>> sum_digits(7)
    7
    >>> sum_digits(123)
    6
    >>> sum_digits(875)
    20
    """
    assert n >= 0 and type(n) == int
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)