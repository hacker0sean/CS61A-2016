def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def fun(f):
        nonlocal n
        n = f(n)
        print(n)
        return memory(n)
    return fun