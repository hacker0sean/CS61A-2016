def multiply(m, n):
    """
    m a product factor
    n a product factor
    return the product of m and n

    >>> multiply(3, 4)
    12
    >>> multiply(1, 12)
    12
    >>> multiply(4, 5)
    20
    """
    if n == 1:
        return m
    else:
        return multiply(m, n - 1) + m