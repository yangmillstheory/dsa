class Solution:
    def _generate(self, n, n_open, n_close, buf, res):
        if n_open == n_close == n:
            res.append(''.join(buf))
        else:
            if n_open < n:
                buf.append('(')
                self._generate(n, n_open+1, n_close, buf, res)
                buf.pop()
            if n_close < n_open:
                buf.append(')')
                self._generate(n, n_open, n_close+1, buf, res)
                buf.pop()
        return res

    def generateParenthesis(self, n):
        return self._generate(n, 0, 0, [], [])


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
