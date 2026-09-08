# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        initial = lists[0]
        for i in range(1, len(lists)):
            head = None
            if initial.val < lists[i].val:
                head = ListNode(initial.val, None)
                initial = initial.next
            else:
                head = ListNode(lists[i].val, None)
                lists[i] = lists[i].next
            pointer = head
            while initial is not None and lists[i] is not None:
                if initial.val < lists[i].val:
                    pointer.next = ListNode(initial.val, None)
                    initial = initial.next
                else:
                    pointer.next = ListNode(lists[i].val, None)
                    lists[i] = lists[i].next
                pointer = pointer.next
            if initial is not None:
                pointer.next = ListNode(initial.val, initial.next)
            else:
                pointer.next = ListNode(lists[i].val, lists[i].next)
            initial = head
        return initial
                    

                
        