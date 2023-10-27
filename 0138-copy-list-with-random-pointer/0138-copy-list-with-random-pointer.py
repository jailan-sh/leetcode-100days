"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = head
        if not head:
            return head

        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        new_head = head.next
        new_cur = new_head
        while cur:
            cur.next = new_head.next
            if new_head.next:
                new_head.next = new_head.next.next
            cur = cur.next
            new_head = new_head.next

        return new_cur

        
