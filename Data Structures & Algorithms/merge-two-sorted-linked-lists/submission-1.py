# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we need a new list
        ourListNode = ListNode()

        #pointer to that list
        tail = ourListNode

        #loop through the linkedlist
        while list1 and list2:

            #if list1 val is less than list2 then attach list1 to the new list first then attach list2
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else: 
                tail.next = list2
                list2 = list2.next
            
            tail= tail.next
            

        #after that while loop
        tail.next = list1 or list2
    
        return ourListNode.next



"""

Runtime -O(n+m) 
Space - O(n+m)



"""







        