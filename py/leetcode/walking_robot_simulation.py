N = (-1, 0)
S = (+1, 0)
E = (0, +1)
W = (0, -1)


class Solution(object):
    class Robot:
        def __init__(self):
            self.pos = (0, 0)
            self.dir = E
            self.obs = set()

        def _turn_left(self):
            if self.dir is N:
                self.dir = W
            elif self.dir is W:
                self.dir = S
            elif self.dir is S:
                self.dir = E
            elif self.dir is E:
                self.dir = N

        def _turn_right(self):
            if self.dir is N:
                self.dir = E
            elif self.dir is E:
                self.dir = S
            elif self.dir is S:
                self.dir = W
            elif self.dir is W:
                self.dir = N

        def _advance(self):
            pos = (
                self.pos[0] + self.dir[0],
                self.pos[1] + self.dir[1]
            )
            if pos in self.obs:
                return False
            self.pos = pos
            return True

        def sq_distance(self):
            return pow(self.pos[0], 2) + pow(self.pos[1], 2)

        def _process(self, command):
            if command == -1:
                self._turn_right()
            elif command == -2:
                self._turn_left()
            else:
                for _ in range(command):
                    ok = self._advance()
                    if not ok:
                        break

        def process(self, commands, obstacles):
            self.obs = set(map(tuple, obstacles))
            for command in commands:
                self._process(command)
                yield self.sq_distance()
            self.obs = set()

    def robotSim(self, commands, obstacles):
        robot = self.Robot()
        return max(robot.process(commands, obstacles))


if __name__ == '__main__':
    s = Solution()
    result = s.robotSim([4, -1, 4, -2, 4], [[2, 4]])
    print(result)
