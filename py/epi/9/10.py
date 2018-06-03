def in_order_successor_with_parents(root):
    '''In-order successor in a binary tree in O(h) time and O(1) space.'''
    if root.right:
        root = root.right
        while root.left:
            root = root.left
        return root
    elif root.parent:
        # this condition isn't really necessary given loop below, but it's clearer this way
        if root.parent.left == root:
            return root.parent
        while root.parent and root.parent.right == root:
            root = root.parent
        return root.parent
