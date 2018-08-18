class Solution(object):
    def numDecodings(self, s):
        memo, n = {}, len(s)

        def n_decodings_from(start):
            # T(n) = O(3^n)
            # S(n) = O(1)
            if start in memo:
                return memo[start]
            if start == n:
                return 1
            count = cand = p = 0
            for j in range(start, min(start+3, n)):
                cand *= pow(10, p)
                cand += int(s[j])
                if cand < 1 or cand > 26:
                    break
                count += n_decodings_from(j+1)
                p += 1
            memo[start] = count
            return count
        return n_decodings_from(0)


if __name__ == '__main__':
    s = Solution()
    s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
    assert s.numDecodings("226") == 3, s.numDecodings("226")
    assert s.numDecodings("12") == 2
