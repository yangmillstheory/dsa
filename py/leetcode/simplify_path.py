import collections


DELIM = '/'


class Solution(object):
    def simplifyPath(self, path):
        # T(n) = S(n) = O(n)
        nodes = collections.deque()
        for node in filter(lambda node: node and node != '.', path.split(DELIM)):
            if node == '..':
                if not nodes or nodes[-1] == '..':
                    nodes.append(node)
                else:
                    nodes.pop()
            else:
                nodes.append(node)
        while nodes and nodes[0] == '..':
            nodes.popleft()
        res = DELIM.join(nodes)
        return DELIM+res if path.startswith(DELIM) else res
