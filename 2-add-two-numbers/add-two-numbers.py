class Solution:  


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
           
        i = 0; 
        num1 = 0; 
        while l1: 
            num1 = num1 + l1.val * 10**i;
            i = i+1; 
            l1 = l1.next; 
        i = 0; 
        num2 = 0; 
        while l2: 
            num2 = num2 + l2.val * 10**i;
            i = i+1; 
            l2 = l2.next; 

        num = num1+num2; 
        if num ==0:
            return ListNode(0)

        root = None; 
        tail = None; 

        while num:
            node = ListNode(num % 10)

            if root is None:
                root = node;
                tail = node;
            else:
                tail.next = node;
                tail = node;

            num //= 10;

        return root