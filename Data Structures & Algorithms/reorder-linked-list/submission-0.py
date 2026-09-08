# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        while head is not None:
            arr.append(head)
            head= head.next
        i, j = 0, len(arr)-1
        while i < j:
            arr[i].next = arr[j]
            i+=1
            if i>=j:
                break
            arr[j].next = arr[i]
            j -= 1
        arr[i].next = None