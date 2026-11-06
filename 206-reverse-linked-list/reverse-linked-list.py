# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        if head == None: 
            return head
        tail = head; 

        val_list = [];
        while tail and tail.next: 
            val_list.append(tail.val)
            tail = tail.next;
        
        newhead = tail; 

        for i in range(len(val_list)-1,-1,-1):
            #print(i)
            tail.next = ListNode(val_list[i])
            #print(newhead)
            #print(tail)
            tail = tail.next;

        
        tail.next = None

        #print(newhead)

        return newhead




            
