def in_order_with_parents(root):
    '''In-order traversal in a tree with parent pointers.

    T(n) = O(n)
    S(n) = O(1)
    '''
    last = None
    while root:
        if last == root.parent:
            while root.left:
                root = root.left
            yield root.data
            last, root = root, root.right or root.parent
        elif last == root.left:
            yield root.data
            last, root = root, root.right or root.parent
        elif last == root.right:
            root = root.parent
