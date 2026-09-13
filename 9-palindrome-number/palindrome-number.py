class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False

        array = []; 
        #j = 0; 

        while x!=0:
            array.append(x%10)
            x = (x - x%10)/10; 
            #print(x)

        #print(array)

        for i in range(0,floor(len(array)/2)):
            if array[i] != array[len(array)-i-1]:
                return False
        

        return True
