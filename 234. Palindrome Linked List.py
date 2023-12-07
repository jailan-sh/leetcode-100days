# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        while head:
            if head.val == stack[-1]:
                stack.pop()
                head = head.next
            else:
                return False
        return True
