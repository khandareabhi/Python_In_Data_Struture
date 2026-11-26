# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        arr=[]

        while head:
            arr.append(head.val)
            head=head.next
        
        return arr==arr[::-1] # this is used to check the palindrome in the linked list if it is same from left to right and right to left then it is palindrome otherwise not

        