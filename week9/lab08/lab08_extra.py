def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_count = 0
    def make_advance():
        count = 0
        def advanced_counter(string):
            nonlocal global_count, count
            if string == 'count':
                count += 1
                return count
            elif string == 'reset':
                count = 0
            elif string == 'global-count':
                global_count += 1
                return global_count
            elif string == 'global-reset':
                global_count = 0
        return advanced_counter
    return make_advance

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    deal = False
    m, n = 1, 1
    while m <= len(first):
        n = 1
        while n <= len(second):
            if sum(first[0: m]) == sum(second[0: n]):
                deal = True
                break
            n = n + 1
        if deal == True:
            break
        m = m + 1
    if deal:
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'

a = [1, 1, 3, 2, 1, 1, 4]
print(sum(a[0:1]))
b = [4, 3, 2, 7]
trade(a, b)

def boom(n):
    sum = 0
    a, b = 1, 1
    while a <= n*n:
        while b <= n*n:
            sum += (a*b)
            b += 1
        b = 0
        a += 1
    return sum