from ucb import trace

# Constructor
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

# 3.1
def square_tree(t):
    """Return a tree with the square of every element in t"""
    if is_leaf(t):
        return tree(root(t) ** 2)
    else:
        return tree(root(t) ** 2, [square_tree(b) for b in branches(t)])

def height(t):
    if is_leaf(t):
        return 1
    else:
        return 1 + max([height(b) for b in branches(t)])

def tree_max(t):
    """Return the max of a tree."""
    if is_leaf(t):
        return root(t)
    else:
        return max([root(t)] + [tree_max(b) for b in branches(t)])

def find_path(tree, x):
    """Return the path from root to x in the tree"""
    if root(tree) == x:
        return [x]
    elif is_leaf(tree):
        return []
    else:
        for b in branches(tree):
            return find_path(b, x) +

t = tree(2,[tree(7,[tree(3),tree(6,[tree(5),tree(11)])]),tree(15)])

print(find_path(t, 5))