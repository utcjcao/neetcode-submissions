# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        current = head
        l = []
        while current != None:
            l.append(current)
            current = current.next
        for i in range(len(l)-1, -1, -1):
            if i-1 != -1:
                l[i].next = l[i-1]
            else:
                l[i].next = None
        return l[-1]
        