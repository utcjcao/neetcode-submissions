# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        visited = set()
        visited.add(head)
        cur = head
        while cur is not None:
            if cur.next in visited:
                return True
            visited.add(cur.next)
            cur= cur.next
        return False
                
