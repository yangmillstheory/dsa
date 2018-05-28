def sum_binary_paths(root, partial_sum=0):
    '''In a tree where a path represents a binary number,
    sum all search paths in O(n) and O(h) time.
    '''
    if not root:
        return 0
    partial_sum *= 2
    partial_sum += root.val
    l, r = root.left, root.right
    return sum_binary_paths(l, partial_sum) + sum_binary_paths(r, partial_sum)
