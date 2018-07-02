ops = {'+', '-', '/', '*'}


def signum(x):
    return -1 if x < 0 else 1


class Solution(object):
    def evalRPN(self, tokens):
        # T(n) = S(n) = O(n)
        nums = []
        for ch in tokens:
            if ch not in ops:
                nums.append(int(ch))
                continue
            b, a = nums.pop(), nums.pop()
            if ch == '+':
                c = a+b
            elif ch == '-':
                c = a-b
            elif ch == '/':
                c = signum(a)*signum(b)*(abs(a)//abs(b))
            elif ch == '*':
                c = a*b
            else:
                raise ValueError(ch)
            nums.append(c)
        return nums.pop()
