def kth_in_order(root, k):
    '''kth node in a binary tree with T(n) = O(h) and S(n) = O(h).'''
    if not root:
        return
    l, r, n = root.left, root.right, root.count
    if l:
        if n-l.n == k:
            return root
        if n-l.n > k:
            return kth_in_order(l, k)
        return kth_in_order(r, k-(n-l.n))
    if k == 1:
        return root
    if r:
        return kth_in_order(r, k-1)


def kth_in_order_iterative(root, k):
    '''kth node in a binary tree with T(n) = O(h) and S(n) = O(1).'''
    while root:
        l_size = root.left.size if root.left else 0
        if l_size+1 == k:
            return root
        elif k <= l_size:
            root = root.left
        else:
            root = root.right
            k -= l_size+1
