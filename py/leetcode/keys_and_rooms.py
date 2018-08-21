class Solution(object):
    def _dfs(self, rooms):
        seen = set()

        def dfs(room):
            seen.add(room)
            while rooms[room]:
                _room = rooms[room].pop()
                if _room in seen or _room == room:
                    continue
                dfs(_room)
        dfs(0)
        return len(seen) == len(rooms)

    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        seen, stack = [False]*n, [0]
        while stack:
            _room = stack.pop()
            seen[_room] = True
            for _next in rooms[_room]:
                if seen[_next]:
                    continue
                stack.append(_next)
        return all(seen)
