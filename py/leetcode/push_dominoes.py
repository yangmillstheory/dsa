class Solution(object):
    def pushDominoes(self, dominoes):
        pushed, n = list(dominoes), len(dominoes)
        i = 0
        while i < n:
            j = i+1
            while j < n and pushed[j] == '.':
                if pushed[i] != 'R' and pushed[j] == 'R':
                    i = j
                j += 1
            if j == n:
                if pushed[i] == 'R':
                    for k in range(i, j):
                        pushed[k] = 'R'
                break
            next_i = j
            if pushed[i] == 'R' and pushed[j] == 'L':
                while i < j:
                    pushed[i], pushed[j] = 'R', 'L'
                    i += 1
                    j -= 1
            elif pushed[i] != 'R' and pushed[j] == 'L':
                for k in range(i, j):
                    pushed[k] = 'L'
            elif pushed[i] == 'R' and pushed[j] != 'L':
                for k in range(i, j):
                    pushed[k] = 'R'
            i = next_i
        return ''.join(pushed)
