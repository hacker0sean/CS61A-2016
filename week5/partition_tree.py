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

def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if root(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(root(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)
print(partition_tree(2, 2))
print_parts(partition_tree(2, 2))