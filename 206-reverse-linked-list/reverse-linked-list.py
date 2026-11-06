# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        if head == None: 
            return head
        
        prev = None
        curr = head

        while curr is not None:

            # 1. Save the next node
            next_node = curr.next

            # 2. Reverse the current link
            curr.next = prev

            # 3. Advance prev
            prev = curr; 

            # 4. Advance curr
            curr = next_node
        

        return prev


            
