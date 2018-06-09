import heapq
import functools


@functools.total_ordering
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __eq__(self, other):
        return self is other


class Solution:
    def mergeKLists(self, lists):
        '''Merge k sorted linked lists in O(n*log k) time and O(k) space.'''
        dummy = tail = ListNode(0)
        heap = [HeapNode(node) for node in lists if node]
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap).node
            tail.next = node
            if node.next:
                heapq.heappush(heap, HeapNode(node.next))
            tail = tail.next
        return dummy.next
