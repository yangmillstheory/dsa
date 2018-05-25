def merge(a, m, b, n):
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
    a = [5, 13, 17, None, None, None, None, None]
    b = [3, 7, 11, 19]
    merge(a, 3, b, 4)
    assert a == [3, 5, 7, 11, 13, 17, 19, None], a
