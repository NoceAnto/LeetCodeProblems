# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        temp = head; 
        i = 1; 
        while temp: 
            temp = temp.next; 
            i = i + 1;

        j = floor((i-1)/2)+1;
        k = 1 
        while head: 
            
            if k == j: 
                return head
            head = head.next; 
            k = k + 1;

                  
        