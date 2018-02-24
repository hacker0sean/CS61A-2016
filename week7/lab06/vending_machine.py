def vending_machine(snacks):
    """Cycles through list of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    state = -1
    def vender():
        nonlocal state
        state = state + 1
        state = state % 3
        return snacks[state]
    return vender
