# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        start = dummy
        while head and head.next:
            pt1 = head
            pt2 = head.next

            start.next = pt2
            pt1.next = pt2.next
            pt2.next = pt1

            start = pt1
            head = pt1.next
            
        return dummy.next
