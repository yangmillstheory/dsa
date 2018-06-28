class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        j = rem = min_rem = 0
        n = len(gas)
        for i in range(1, n):
            rem += gas[i-1] - cost[i-1]
            if rem < min_rem:
                j, min_rem = i, rem
        return j
