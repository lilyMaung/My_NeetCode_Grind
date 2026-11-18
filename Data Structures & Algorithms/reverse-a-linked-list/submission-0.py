# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initializing the pointers
        prev = None
        curr = head

        while curr:
            #saving the next pointer to not Lose the data
            nxt = curr.next
        
            #then change the pointer 
            curr.next = prev

            prev = curr

            curr = nxt

            #now prev is the head now so return prev

        return prev
        
        
        