# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        prev = None
        cur = second
        while cur:
            second = cur.next
            cur.next = prev
            prev = cur
            cur = second
        second = prev

        first = head
        while second:
            nfirst = first.next
            nsecond = second.next
            first.next = second
            second.next = nfirst
            first = nfirst
            second = nsecond

        return head


