import collections


def _is_leaf(root):
    return not root.left and not root.right


def print_left(root):
    while root and not _is_leaf(root):
        print(root.data)
        if root.left:
            root = root.left
        else:
            root = root.right


def print_leaves(root):
    # inorder walk
    stack = collections.deque()
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if _is_leaf(root):
                print(root.data)
            root = root.right


def print_right(root):
    # reverse inorder walk
    stack = collections.deque()
    while root:
        stack.append(root)
        if root.right:
            root = root.right
        else:
            root = root.left
    # remove single leaf
    stack.pop()
    while stack:
        root = stack.pop()
        assert not _is_leaf(root)
        print(root.data)


def print_exterior(root):
    '''Print the exterior of a binary tree in O(n) time and O(h) space.'''
    print_left(root)
    print_leaves(root)
    print_right(root)
