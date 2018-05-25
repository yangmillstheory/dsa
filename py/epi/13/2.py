def merge(a, b):
    n = len(b)
    for j in range(n):
        a[n+j], a[j] = a[j], b[j]
    i = n
    j = 0
    k = 0
    while a[k] is not None:
        if a[i] is None:
            a[k] = b[j]
            j += 1
        elif b[j] is None:
            a[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            a[k] = a[i]
            i += 1
        else:
            a[k] = b[j]
            j += 1
        k += 1
    return a


if __name__ == '__main__':
    a = [5, 13, 17, None, None, None, None, None]
    b = [3, 7, 11, 19]

    assert merge(a, b) == [3, 5, 7, 11, 13, 17, 19, None]
