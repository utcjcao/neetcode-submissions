# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        head = cur
        carry = 0
        while l1 or l2 or carry:
            if (l1):
                cur.val += l1.val
            if (l2):
                cur.val += l2.val
            cur.val += carry
            carry = 0
            if cur.val >= 10:
                carry = cur.val//10
            cur.val %= 10
            new = ListNode()
            if (carry):
                cur.next = new
                cur = cur.next
            elif (l1 and l1.next):
                cur.next = new
                cur = cur.next
            elif (l2 and l2.next):
                cur.next = new
                cur = cur.next
                
            if (l1):
                l1 = l1.next
            if (l2):
                l2 = l2.next
        return head