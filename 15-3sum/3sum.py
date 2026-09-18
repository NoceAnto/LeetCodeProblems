class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        output = [];
        outset = [];

        nums.sort()#O(logn)
        #print(nums)
        
        #O(n2)
        # fix one number 
        for i in range(0,len(nums)): #O(n)

            if i>0 and nums[i-1] == nums[i]: 
                #print("Iteration "+str(i)+": same num as before")
                continue; 

            # 2sum problem 
            newtarget = 0 - nums[i]; 
            #print("Iteration "+str(i)+": target 2sum "+str(newtarget)+"\n")
            
            seen = set(); 

            for j in range(i+1,len(nums)): #O(n)
                #print("--Nested Iteration "+str(j)+": checking "+str(nums[j])+"\n")
                #print("Have I seen previously "+ str(newtarget - nums[j])+"?")
                
                if j>=3 and nums[j] == nums[j-1] and nums[j-1]==nums[j-2] and nums[j-2] == nums[j-3]:
                    #print("4 consecutive "+str(nums[j])+"- skip")

                    continue;
                    
                if newtarget - nums[j] in seen: #O(1)

                    ans = [nums[i],newtarget - nums[j],nums[j]]; 
                    #print("YES--- answer "+str(ans))

                    output.append(ans)

                    seen.remove(newtarget - nums[j])
                    #if nums[j] == nums[j-1]:
                    #    continue 
                else: 
                    seen.add(nums[j]) #O(1)
                    #print("NO--- adding in seen "+str(nums[j]))

                       
        return output 
