# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointer to traverse the list
        current = dummy
        
        # Traverse and remove matching nodes
        while current.next:
            if current.next.val == val:
                # Skip the node with value == val
                current.next = current.next.next
            else:
                current = current.next
        
        # Return new head (could have changed)
        return dummy.next
        
