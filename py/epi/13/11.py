def find_salary_cap(xs, t):
    xs.sort()
    n = len(xs)
    raw = 0
    for j, x in enumerate(xs):
        adj = (n-j)*x
        if raw + adj >= t:
            return (t-raw)/(n-j)
        raw += x
    return -1


if __name__ == '__main__':
    xs, t = [90, 30, 100, 40, 20], 210
    c = find_salary_cap(xs, t)
    assert c == 60, c
