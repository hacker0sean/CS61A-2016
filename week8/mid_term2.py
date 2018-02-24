gold = [0 , 1]
def go ( dream , team ):
    print ( 'Steps to success :' )
    def medal ( lion ):
        return dream (team , lion )
    return medal
def win(big ):
    print ( 'Eat vegetables .')
    return big [ -1] + big [ -2]
def get ( it , done ):
    do = it
    while done < 2:
        print ("Don ’t cheat !")
        do , done = do + [win(do)], done + 1
    return do


#Q4
def is_sorted ( n ):
    """ Returns whether the digits in n are in non - increasing order
    from left to right .
    >>> is_sorted (4)
    True
    >>> is_sorted (55555)
    True
    >>> is_sorted (9876543210)
    True
    >>> is_sorted (9087654321)
    False
    """
    if n // 10 == 0:
        return True
    elif n // 10 % 10 >= n % 10:
        return is_sorted(n // 10)
    else:
        return False

#Q5 . a
def aggregate ( fn , seq , pred ):
    """ Aggregates using fn the elements in seq that satisfy pred .
    >>> def is_even (x):
    ...     return x % 2 == 0
    >>> def sum_plus_one (x, y):
    ...     return x + y + 1
    >>> aggregate ( sum_plus_one , [2 , 4 , 6] , is_even ) # (2 + 4 + 1) + 6 + 1
    14
    >>> # If no elements satisfy pred , return None
    >>> aggregate ( sum_plus_one , [1 , 3 , 5 , 7 , 9] , is_even )
    >>> # If only one element satisfies pred , return that element
    >>> aggregate ( sum_plus_one , [1 , 2 , 3] , is_even )
    2
    """
    result = None
    lis = [i for i in seq if pred(i)]
    while len(lis) > 1:
        lis[0] = fn(lis[0], lis[1])
        del(lis[1])
    if len(lis) == 1:
        result = lis[0]
    return result
#Q5 .b
from operator import add, mul
fact = lambda x : aggregate(mul, range(1, x + 1), lambda _: True) if x != 0 else 1


#Q6
empty = 'empty'
def link (first , rest = empty ):
    return [first , rest ]
def first (lnk ):
    return lnk [0]
def rest (lnk ):
    return lnk [1]

def linked_sum ( lnk , total ):
    """ Return the number of combinations of elements in lnk that
    sum up to total .
    >>> # Four combinations : 1 1 1 1 , 1 1 2 , 1 3 , 2 2
    >>> linked_sum ( link (1 , link (2 , link (3 , link (5)))) , 4)
    4
    >>> linked_sum ( link (2 , link (3 , link (5))) , 1)
    0
    >>> # One combination : 2 3
    >>> linked_sum ( link (2 , link (4 , link (3))) , 5)
    1
    """
    if total == 0:
        return 1
    elif lnk == empty:
        return 0
    else :
        with_first = sum([linked_sum(rest(lnk), total - first(lnk) * i) for i in range(1, (total // first(lnk)) + 1)])
        without_first = linked_sum(rest(lnk), total)
        return with_first + without_first


def tree(entry, children=[]):
    return [entry, children]
def entry ( tree ):
    return tree[0]
def children ( tree ):
    return tree[1]

def track_lineage ( family_tree , name ):
    """ Return the entries of the parent and grandparent of
    the node with entry name in family_tree .
    >>> t = tree ( "Tytos", [tree ( "Tywin", [tree ( "Cersei") , tree ( "Jaime") , tree ( "Tyrion")]) ,tree ( "Kevan", [tree ( "Lancel") , tree ( "Martyn") , tree ("Willem")])])
    >>> track_lineage (t, "Cersei")
    ["Tywin", "Tytos"]
    >>> track_lineage (t, "Tywin")
    [ "Tytos", None ]
    >>> track_lineage (t, "Tytos")
    [None , None ]
        """
    def tracker(t, p, gp):
        if name == entry(t):
            return [p, gp]
        for c in children (t):
            res = tracker(c, entry(t), p)
            if res:
                return res
    return tracker(family_tree, None, None)

def are_cousins ( family_tree , name1 , name2 ):
    """ Return True if a node with entry name1 is a cousin of a node with
    entry name2 in family_tree .
    >>> are_cousins(t, "Kevan", "Tytos") # same tree as before
    False
    >>> are_cousins(t, "Cersei", "Lancel")
    True
    >>> are_cousins(t, "Jaime", "Lancel")
    True
    >>> are_cousins(t, "Jaime", "Tyrion")
    False
    """
    p1, gp1 = track_lineage(family_tree, name1)
    p2, gp2 = track_lineage(family_tree, name2)
    return p1 != p2 and gp1 == gp2 and gp1 != None