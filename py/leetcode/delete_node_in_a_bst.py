class Solution(object):
    def _delete_and_return_min(self, tree):
        '''Deletes and returns the minimum node in a non-empty binary tree in O(h) time.'''
        prev = None
        while tree and tree.left:
            prev, tree = tree, tree.left
        if prev:
            prev.left = tree.right
        return tree

    def deleteNode(self, tree, key):
        '''Deletes a node from a BST in O(h) time and O(1) space. The key doesn't have to exist in the tree.'''
        prev, root = None, tree
        while tree:
            if tree.val == key:
                break
            if tree.val < key:
                prev, tree = tree, tree.right
            else:
                prev, tree = tree, tree.left
        if not tree:
            return root
        if tree.right:
            repl = self._delete_and_return_min(tree.right)
            repl.left = tree.left
            if repl != tree.right:
                repl.right = tree.right
        else:
            repl = tree.left
        if prev:
            if prev.val > key:
                prev.left = repl
            else:
                prev.right = repl
            return root
        return repl
