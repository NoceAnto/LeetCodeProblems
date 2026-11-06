# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        
        if head.next is None: 
            head = None; 
            return head 

        if head.next.next is None: 
            head.next = None; 
            return head 
        
        slow = head; 
        fast = head; 
        prev = None; 

        while fast is not None and fast.next is not None:
            prev = slow;
            slow = slow.next; 
            fast = fast.next.next; 

            #print(slow)
            #print(fast)
            #print(prev)

        
        prev.next = prev.next.next; # eliminate middle node ?? 

        return head 

