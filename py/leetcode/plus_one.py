class Solution(object):
    def plusOne(self, a):
        carry = 1
        for i in range(len(a)-1, -1, -1):
            digit = a[i]
            digit += carry
            if digit >= 10:
                a[i], carry = 0, 1
            else:
                a[i] = digit
                break
        else:
            if carry == 1:
                a[0] = 1
                a.append(0)
        return a
