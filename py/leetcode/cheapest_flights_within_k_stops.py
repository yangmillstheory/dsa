import collections


class Solution(object):
    def __init__(self):
        self._min_cost = float('inf')

    def findCheapestFlight(self, *args):
        return self._bfs(*args)

    def _dfs(self, n, flights, src, dst, max_stops):
        flights_by_city = collections.defaultdict(list)
        for _src, _dst, cost in flights:
            flights_by_city[_src].append((_dst, cost))

        def dfs(city, cost, stops):
            if city == dst:
                self._min_cost = min(self._min_cost, cost)
            elif stops <= max_stops:
                stops += 1
                for _city, _cost in flights_by_city[city]:
                    cost_to_dest = cost + _cost
                    if cost_to_dest >= self._min_cost:
                        continue
                    dfs(_city, cost_to_dest, stops)
        dfs(src, 0, 0)
        return self._min_cost if self._min_cost != float('inf') else -1

    def _bfs(self, n, flights, src, dst, max_stops):
        '''Find the cheapest cost from source City to destination City in O(n) time and space.'''
        flights_by_city = collections.defaultdict(list)
        for _src, _dst, cost in flights:
            flights_by_city[_src].append((_dst, cost))
        q = collections.deque([(src, 0, 0)])
        while q:
            city, cost, stops = q.pop()
            stops += 1
            for _city, _cost in flights_by_city[city]:
                next_cost = cost + _cost
                if next_cost >= self._min_cost or stops > max_stops:
                    continue
                q.append((_city, next_cost, stops))
        return self._min_cost if self._min_cost != float('inf') else -1
