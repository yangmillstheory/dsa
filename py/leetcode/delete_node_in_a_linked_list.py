class Solution(object):
    def deleteNode(self, node):
        # given: node is not the tail
        node.val = node.next.val
        node.next = node.next.next

