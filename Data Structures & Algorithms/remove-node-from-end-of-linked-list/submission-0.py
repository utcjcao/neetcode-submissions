# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        q = head
        while q is not None:
            q = q.next
            l += 1
        f = l-n
        
        if f==0:
            head = head.next
            return head
        cur = head
        while f > 1:
            cur = cur.next
            f -= 1
        cur.next = cur.next.next
        return head