class Solution:
    def merge(self, a, m, b, n):
        k = m-1
        for i in range(m+n-1, n-1, -1):
            a[i] = a[k]
            k -= 1
        for j in range(n):
            a[j] = b[j]
        i = n
        j = 0
        for k in range(m+n):
            if i == m+n:
                a[k] = b[j]
                j += 1
            elif j == n:
                a[k] = a[i]
                i += 1
            elif a[i] < b[j]:
                a[k] = a[i]
                i += 1
            else:
                a[k] = b[j]
                j += 1
            k += 1


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    Solution().merge(a, 3, b, 3)
    assert a == [1, 2, 2, 3, 5, 6], a

    a = [0]
    b = [1]
    Solution().merge(a, 0, b, 1)
    assert a == [1], a

    a = [1, 2, 4, 5, 6, 0]
    b = [3]
    Solution().merge(a, 5, b, 1)
    assert a == [1, 2, 3, 4, 5, 6], a
