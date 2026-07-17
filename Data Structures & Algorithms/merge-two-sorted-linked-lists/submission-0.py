# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2

        root = ListNode(0)
        now = root

        while curr1 and curr2:
            if curr1.val < curr2.val:
                now.next = curr1
                now = curr1
                curr1 = curr1.next
            else:
                now.next = curr2
                now = curr2
                curr2 = curr2.next

        if curr1:
            now.next = curr1
        else:
            now.next = curr2

        return root.next