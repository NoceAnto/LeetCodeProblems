class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0: 
            return nums
        
        i = 0; 
        j = 1; 

        #print(nums)
        #print(len(nums))

        while i<j and i<len(nums) and j<len(nums): 
            #print("Numeri:"+str(nums[i])+" "+str(nums[j])+"; indici:"+str(i)+","+str(j))

            if nums[i]==0 and nums[j]!=0:
                #print("Numero in index "+str(i)+" is zero and in index "+str(j)+" is not zero")
                nums[i] = nums[j]; 
                nums[j] = 0; 
                #print(nums)
                i = i+1; 
                j = j+1; 
                #print(i,j)
                continue;

            if nums[i]!=0 and nums[j]!=0: 
                #print("Numero in index "+str(i)+" is not zero and in index "+str(j)+" is not zero")
                i = i+2; 
                j = j+2;
                continue;
            
            if nums[i]!=0 and nums[j]==0: 
                #print("Numero in index "+str(i)+" is not zero and in index "+str(j)+" is zero")
                i = i+1; 
                j = j+1; 
                continue;
            
            if nums[i]==0 and nums[j]==0: 
                #print("Numero in index "+str(i)+" is zero and in index "+str(j)+" is zero")
                j = j+1; 
                continue;
            #print(nums[i],nums[j],i,j)

        return nums
             
