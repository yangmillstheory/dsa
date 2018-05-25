def intersection(a, b):
    """Returns the intersection of two sorted lists
    in O(m + n) time.

    """
    m, n = len(a), len(b)
    i = j = 0
    res = []
    while i < m and j < n:
        if a[i] > b[-1] or b[j] > a[-1]:
            break
        elif a[i] == b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return res


def main():
    a = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    b = [5, 5, 6, 8, 8, 9, 10, 10]
    assert intersection(a, b) == [5, 6, 8]

    a = [1]
    b = [1, 1]
    assert intersection(a, b) == [1]

    a = [1, 2]
    b = [3, 4]
    assert intersection(a, b) == []


if __name__ == '__main__':
    main()
