# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = None
        prevHead = None
        cur = head
        while cur:
            c = 0
            checker = cur
            while (checker and c < k):
                checker = checker.next
                c+=1
            if (c != k):
                prevHead.next = cur
                return ans
                # attach oldhead.next to next in line.
            
            sCur = cur
            initHead = cur
            prev = None            
            c = 0
            while (c < k):
                next = sCur.next
                sCur.next = prev
                prev = sCur
                sCur = next
                
                c+=1
            if (prevHead):
                prevHead.next = prev
    
            if (ans is None):
                ans = prev
            prevHead = initHead
            cur = sCur
            # print('iterated')
        return ans

        # since we also want to connect first to last, 
        # when we finish reversing k nodes, we connect prev head to cur tail
        # set prev head to cur head. 
