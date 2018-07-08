class Solution(object):
    def _delete_and_return_min(self, tree):
        '''Deletes and returns the minimum node in a non-empty binary tree in O(h) time.'''
        prev = None
        while tree and tree.left:
            prev, tree = tree, tree.left
        if prev:
            prev.left = tree.right
        return tree

    def _find_with_prev(self, tree, key):
        prev = None
        while tree:
            if tree.val == key:
                break
            if tree.val < key:
                prev, tree = tree, tree.right
            else:
                prev, tree = tree, tree.left
        return tree, prev

    def deleteNode(self, tree, key):
        '''Deletes a node from a BST in O(h) time and O(1) space. The key doesn't have to exist in the tree.'''
        root = tree
        tree, prev = self._find_with_prev(tree, key)
        if not tree:
            return root
        if tree.right:
            repl = self._delete_and_return_min(tree.right)
            repl.left = tree.left
            if repl != tree.right:
                # special case: the minimum of any tree could be its root;
                # we avoid that case since otherwise we'd create a cycle
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
