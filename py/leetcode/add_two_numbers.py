class Solution(object):
    def addTwoNumbers(self, x, y):
        # T(n) = O(n)
        # S(n) = O(1)
        dummy = node = ListNode(0)
        carry = 0
        while x or y or carry:
            x_val = x.val if x else 0
            y_val = y.val if y else 0
            s = x_val + y_val + carry
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            node.next = ListNode(s)
            x = x and x.next
            y = y and y.next
            node = node.next
        return dummy.next
