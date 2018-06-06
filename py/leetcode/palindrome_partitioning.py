def _is_pali(string):
    i = 0
    j = len(string)-1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def partition(self, string):
        return self._partition(string, 0, [], [])

    def _partition(self, string, start, buf, res):
        n = len(string)
        if start >= n:
            res.append(buf[:])
        else:
            for j in range(start, n):
                cand = string[start:j+1]
                if _is_pali(cand):
                    buf.append(cand)
                    self._partition(string, j+1, buf, res)
                    buf.pop()
        return res
