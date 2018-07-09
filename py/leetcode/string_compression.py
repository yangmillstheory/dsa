TERM = '-'


class Solution(object):
    def _compress_wo_sentinel(self, chars):
        '''Run-length compression on a list of characters in O(n) time and O(1) space.'''
        n = len(chars)
        i, count = 0, 1
        for j in range(1, n+1):
            if j < n and chars[j] == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for d in str(count):
                        chars[i] = d
                        i += 1
                count = 1
        return i

    def _compress_w_sentinel(self, chars):
        '''Run-length compression on a list of characters in O(n) time and O(1) space.'''
        i = count = 0
        chars.append(TERM)
        for j, ch in enumerate(chars):
            if j == 0 or ch == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for d in str(count):
                        chars[i] = d
                        i += 1
                count = 1
        chars.pop()
        return i

    def compress(self, chars):
        return self._compress_wo_sentinel(chars)

