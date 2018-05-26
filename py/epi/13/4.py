def smallest_non_constructible_value(xs):
    '''Finds the smallest poz. integer that's not
    a subset sum of xs. xs is assumed to be sorted.

    O(n) time
    O(1) space
    '''
    out = 1
    for x in xs:
        if x <= out:
            out += x
        else:
            break
    return out


if __name__ == '__main__':
    x = []
    y = smallest_non_constructible_value(x)
    assert y == 1, y

    x = [1, 3, 6, 10, 11, 15]
    y = smallest_non_constructible_value(x)
    assert y == 2, y

    x = [1, 1, 1, 1]
    y = smallest_non_constructible_value(x)
    assert y == 5, y

    x = [1, 2, 5, 10, 20, 40]
    y = smallest_non_constructible_value(x)
    assert y == 4, y

    x = [1, 2, 3, 4, 5, 6]
    y = smallest_non_constructible_value(x)
    assert y == 22, y
