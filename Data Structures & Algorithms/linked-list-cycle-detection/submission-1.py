# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Given: the head of the linked list
        # return True if we detect a cycle in the linked list or else false
        #if at least one node in the list can be visited again by following the next pointer then we know there is a cycle
        # index is the index of the beginning of the cycle
        #the tail node of the list will set it's next pointer to the indexth node
        # if index = -1 or tail node points to null and then no cycle

        #edge case
        if head == None:
            return False
        
        # two pointers method
        slow = head
        fast = head

        #set to keep track of already seen node
        seen = set()

        while fast != None and fast.next != None:

            slow = slow.next
            fast= fast.next.next
            seen.add(fast)

            if fast is slow and seen:
                return True
            

    
        return False






    














        