# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head) -> int:
        bin_num = ''
        while head:
            bin_num += str(head.val)
            head = head.next
        return int(bin_num, 2)
