class Solution(object):
    def _backtrack(self, s):
        memo, n = {}, len(s)

        def n_decodings_from(start):
            # T(n) = O(3^n)
            # S(n) = O(1)
            if start in memo:
                return memo[start]
            if start == n:
                return 1
            count = cand = p = 0
            for j in range(start, min(start+2, n)):
                cand *= pow(10, p)
                cand += int(s[j])
                if cand < 1 or cand > 26:
                    break
                count += n_decodings_from(j+1)
                p += 1
            memo[start] = count
            return count
        return n_decodings_from(0)

    def _dp(self, s):
        # T(n) = O(n)
        # S(n) = O(1)
        a, b = 0, 1
        for i, ch in enumerate(s):
            c = b if ch != '0' else 0
            if i-1 >= 0 and '0' < s[i-1] < '3' and 1 <= 10*int(s[i-1]) + int(ch) <= 26:
                c += a
            a, b = b, c
        return b

    def numDecodings(self, s):
        return self._dp(s)


if __name__ == '__main__':
    s = Solution()
    assert s.numDecodings('0') == 0
    assert s.numDecodings('226') == 3
    assert s.numDecodings('01') == 0
