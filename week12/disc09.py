def gen_naturals():
    current = 0
    while True:
        yield current
        current += 1
def combiner(iterator1, iterator2, combiner):
    """
    >>> from operator import add
    >>> evens = combiner(gen_naturals(), gen_naturals(), add)
    >>> next(evens)
    0
    >>> next(evens)
    2
    >>> next(evens)
    4
    """
    try:
        while True:
            i1 = next(iterator1)
            i2 = next(iterator2)
            yield combiner(i1, i2)
    except:
        return

def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> print(next(subsets))
    [[]]
    >>> print(next(subsets))
    [[], [1]]
    >>> print(next(subsets))
    [[], [1], [2], [1, 2]]
    """
    disc = {}
    def subsets(n):
        if n == 0:
            return [[]]
        else:
            return disc[n - 1] + [i + [n] for i in disc[n - 1]]
    n = 0
    while True:
        sets = subsets(n)
        disc[n] = sets
        yield sets
        n = n + 1