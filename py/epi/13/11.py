def find_salary_cap(xs, t):
    xs.sort()
    s, n = sum(xs), len(xs)
    j = n-1
    while j >= 0:
        s -= xs[j]
        if j >= 1 and t-s >= xs[j-1]:
            return (t-s)/(n-j)
        j -= 1
    return -1


if __name__ == '__main__':
    xs, t = [90, 30, 100, 40, 20], 210
    c = find_salary_cap(xs, t)
    assert c == 60, c
