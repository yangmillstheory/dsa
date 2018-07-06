# There are 10 people at a wizard meetup.
# Each wizard has levels 0 - 9 (the index of the input) and
# knows a few other wizards there.
# Your job is to find the cheapest way for wizard 0 to meet wizard 9.
# Introductions have a cost that equals the square of the difference in levels.

# Goal: Level 0 wizard wants to meet level 9 using the fewest possible magic points.
# Cost: square of difference of levels
# The index of the array represents the level (0-9)
# the value is an array with the index of the other people each person knows.
# Note that relationships are one directional (e.g. 2 can introduce you to 3 but not vice versa)
# e.g. Min cost: 22 Min path: [0, 1, 4, 6, 9]
from contextlib import contextmanager


@contextmanager
def candidate(path, used, i):
    path.append(i)
    used.add(i)
    yield
    used.remove(i)
    path.pop()


def solve(wizards, i, path, used, curr, cost):
    with candidate(path, used, i):
        if i == len(wizards)-1 and curr < cost['value']:
            cost['path'], cost['value'] = path[:], curr
        else:
            for j in wizards[i]:
                penalty = pow(j-i, 2) if j not in wizards[0] else 0
                if j in used or curr+penalty > cost['value']:
                    continue
                solve(wizards, j, path, used, curr+penalty, cost)


if __name__ == '__main__':
    wizards = [
        [1, 2, 3],
        [8, 6, 4],
        [7, 8, 3],
        [8, 1],
        [6],
        [8, 7],
        [9, 4],
        [4, 6],
        [1],
        [1, 4],
    ]
    cost = {'value': float('inf'), 'path': []}
    solve(wizards, 0, [], set(), 0, cost)
    assert cost == {'value': 22, 'path': [0, 1, 4, 6, 9]}, cost
