from ucb import trace
def count_stair_ways(n):
    """
    I want to go up a flight of stairs that has n steps. I can either take 1 or 2 steps each
    time. How many different ways can I go up this flight of stairs?
    count_stair_ways solves the problem above. It returns the number of ways of the stairs that has n steps

    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(1)
    1
    """
    assert n >= 0 and type(n) == int
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

#@trace
def count_k(n, k):
    """
    A special version of the count stairways problem, where instead of taking
    1 or 2 steps, we are able to take up to and including k steps at a time.

    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    i = 1
    while i <= k:
        total += count_k(n - i, k)
        i = i + 1
    return total