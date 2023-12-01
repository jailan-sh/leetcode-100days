# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a1 = headA
        b2 = headB
        while a1 != b2:
            a1 = headB if a1 is None else a1.next
            b2 = headA if b2 is None else b2.next

        return a1
