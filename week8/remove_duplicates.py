class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)
    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first,repr(self.rest))

def extend_links(l1, l2):
    if l1 == Link.empty:
        return l2
    else:
        return Link(l1.first, extend_links(l1.rest, l2))


def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> len(unique)
    2
    >>> len(lnk)
    2
    """
    if lnk == Link.empty:
        return
    lis = [lnk.first]
    i = 0
    while i < len(lnk):
        if lnk.rest.first not in lis:
            lis.append(lnk.rest.first)
        else:
            lnk.rest = lnk.rest.rest
        i += 1
    return lnk

def reverse(lnk):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> r = reverse(a)
    >>> r.first
    3
    >>> r.rest.first
    2
    """
    if lnk.rest == Link.empty:
        return lnk.first
    else:
        return Link(reverse(lnk.rest), Link(lnk.first))

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    length = min([len(i) for i in lst_of_lnks])
    lis = []
    for i in range(length):
        multiply_element = 1
        for j in range(len(lst_of_lnks)):
            multiply_element *= lst_of_lnks[j][i]
        lis.append(multiply_element)

    def list_to_link(lst):
        """Takes a Python list and returns a Link with the same elements.

        >>> link = list_to_link([1, 2, 3])
        >>> print_link(link)
        <1 2 3>
        """
        if lst == Link.empty:
            return Link.empty
        elif len(lst) == 1:
            return Link(lst[0])
        else:
            return Link(lst[0], list_to_link(lst[1:]))

    return list_to_link(lis)

def foo(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> foo(x)
    [0, 6, 20]
    """
    return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if lst == []:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        return max(max_product(lst[1:]), lst[0] * max_product(lst[2:]))

def tree(root, branches=[]):
    return [root] + list(branches)


# Selectors
def root(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True


def eval_tree(tree):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if type(root(tree)) == int:
        return root(tree)
    elif root(tree) == '+':
        pattern = 0
        result = 0
    elif root(tree) == '*':
        pattern = 1
        result = 1
    for i in branches(tree):
        temp = eval_tree(i)
        if pattern == 0:
            result += temp
        elif pattern == 1:
            result *= temp
    return result


def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) == 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)


def quicksort_link(link):
    """
    >>> s = Link(3, Link(1, Link(4)))
    >>> quicksort_link(s)
    Link(1, Link(3, Link(4)))
    """
    if link == Link.empty:
        return link
    if link.rest == Link.empty:
        return link
    pivot, link = link.first, link.rest
    less, greater = Link.empty, Link.empty
    while link is not Link.empty:
        curr, rest = link, link.rest
        if curr.first < pivot:
            less = Link(curr.first, less)
        else:
            greater = Link(curr.first, greater)
        link = rest
    return extend_links(extend_links(quicksort_link(less), Link(pivot)), quicksort_link(greater))


