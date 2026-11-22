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

        # looping through the linked list until either we reached the end of the list or reach a cycle
        while fast != None and fast.next != None:

            #slow is moving one step by one step 
            slow = slow.next
            #fast is moving two steps at a time
            fast= fast.next.next
            # we put it in the set
            seen.add(fast)

            #finally, if fast reaches the end and it points back to slow and it's also in the set that we have seen, that means we have a cycle 
            if fast is slow and seen:
                return True
    
        return False

    """
    Runtime - O(n) Since we have to go through the whole list
    Space - O(1) 

    Hashset approach:   1 node → 1 entry in the set
                    1,000,000 nodes → 1,000,000 entries      → O(n)

    Tortoise and hare:  1 node → slow, fast
                    1,000,000 nodes → still just slow, fast  → O(1)


    """





    














        