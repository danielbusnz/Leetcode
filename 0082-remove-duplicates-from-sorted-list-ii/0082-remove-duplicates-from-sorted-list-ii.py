# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        current = dummy

        while head:
            if head.next and head.val == head.next.val:
                duplicate = head.val

                while head and head.val == duplicate:
                    head = head.next

                current.next = head
            
            else:
                current = head

                head = head.next
        
        return dummy.next