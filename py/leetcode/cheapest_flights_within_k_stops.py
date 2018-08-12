import collections


City = collections.namedtuple('City', ['index', 'destinations'])
Destination = collections.namedtuple('Destination', ['city', 'cost'])


def _build_cities(n, flights):
    cities = [None]*n
    for src, dst, cost in flights:
        cities[src] = cities[src] or City(src, [])
        cities[dst] = cities[dst] or City(dst, [])
        cities[src].destinations.append(Destination(cities[dst], cost))
    return cities


class Solution(object):
    def __init__(self):
        self._min_cost = float('inf')

    def findCheapestPrice(self, n, flights, src, dst, max_stops):
        '''Find the cheapest cost from source City to destination City in O(n) time and space.'''
        cities = _build_cities(n, flights)

        def dfs(city, cost, stops):
            if city.index == dst:
                self._min_cost = min(self._min_cost, cost)
            elif stops <= max_stops:
                stops += 1
                for _city, _cost in city.destinations:
                    cost_to_dest = cost + _cost
                    if cost_to_dest > self._min_cost:
                        continue
                    dfs(_city, cost_to_dest, stops)
        dfs(cities[src], 0, 0)
        return self._min_cost if self._min_cost != float('inf') else -1
