# Extra Questions

# Q8
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    yield from map(lambda x: x * k, s)

# Q9
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    pre = None
    while True:
        if e0 < e1 and pre != e0:
            pre = e0
            yield e0
            e0 = next(i0)
        elif e0 > e1 and pre != e1:
            pre = e1
            yield e1
            e1 = next(i1)
        else:
            if pre != e0:
                pre = e0
                yield e0
            e0 = next(i0)
            e1 = next(i1)

# Q10
def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    generator = []
    def make_generator(a, m):
        yield a
        yield from make_generator(a + m, m)
    for i in range(m):
        generator.append(make_generator(i, m))
    return generator

# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

# Q11
def zip(*iterables):
    """
    Takes in any number of iterables and zips them together. 
    Returns a generator that outputs a series of lists, each 
    containing the nth items of each iterable. 
    >>> z = zip([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    length = len(iterables)
    i = 0
    try:
        while True:
            lst = []
            for j in iterables:
                lst.append(j[i])
            yield lst
            i = i + 1
    except:
        return
zip([1, 2, 3], [4, 5, 6], [7, 8])