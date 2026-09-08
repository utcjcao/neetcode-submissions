# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        starter = None

        if list1.val > list2.val:
            starter = ListNode(list2.val, None)
            list2 = list2.next
        else:
            starter = ListNode(list1.val, None)
            list1 = list1.next

        head = starter
        
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                starter.next = ListNode(list2.val, None)
                list2 = list2.next
            else:
                starter.next = ListNode(list1.val, None)
                list1 = list1.next
            starter = starter.next
        
        if list1 is None:
            starter.next = list2
        else:
            starter.next = list1

        return head