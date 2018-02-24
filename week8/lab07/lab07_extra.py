from lab07 import *

# Q6
def reverse_other(t):
    """Reverse the roots of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    if t.is_leaf():
        return
    else:
        i , j = 0, len(t.branches) - 1
        while i < j:
            t.branches[i].root, t.branches[j].root = t.branches[j].root, t.branches[i].root
            i, j = i + 1, j - 1
        for i in t.branches:
            reverse_other(i)

# Q7
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
        return t.root
    else:
        for b in t.branches:
            cumulative_sum(b)
        t.root = t.root + sum([b.root for b in t.branches])


t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
cumulative_sum(t)
# Q8
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    n o use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print_link(link1)
    <9 <16> 25 36>
    """
    if link == Link.empty:
        return
    else:
        if isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
        else:
            link.first = fn(link.first)
        deep_map_mut(fn, link.rest)
# Q9
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    lis = []
    while link != Link.empty:
        if link not in lis:
            lis.append(link)
        else:
            return True
        link = link.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    if link is Link.empty:
        return False
    slow, fast = link, link.rest
    while fast is not Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast == slow or fast.rest == slow:
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest
    return False


