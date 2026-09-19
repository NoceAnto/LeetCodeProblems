class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        output = []; 
        # fix a and it is a 3sum 
        #print(nums)

        for a in range(0,len(nums)): 
            if a>0 and nums[a] == nums[a-1]: 
                #print("SKIP - nums[a-1] equal to nums[a]:"+str(nums[a]))
                continue;

            #print("First number:"+str(nums[a]))
            #3 sum 
            for b in range(a+1,len(nums)): 
                if b>a+1 and nums[b] == nums[b-1]: 
                    #print("SKIP - nums[b-1] equal to nums[b]:"+str(nums[a]))
                    continue;

                #print("Second number:"+str(nums[b]))

                c = b+1; 
                d = len(nums)-1; 
                while c<d: 
                    if d<len(nums)-1 and nums[d] == nums[d+1]: 
                        d = d-1; 
                        #print("SKIP - nums[d+1] equal to nums[d]:"+str(nums[d]))
                        continue;

                    if c>b+1 and nums[c] == nums[c-1]:
                        c = c +1; 
                        #print("SKIP - nums[c-1] equal to nums[c]:"+str(nums[c]))
                        continue;
                    
                    #print("Third and fourth numbers:"+str(nums[c])+" and "+str(nums[d])+"; indices "+str(c)+" and"+str(d))

                    o = nums[a]+nums[b]+nums[c]+nums[d]; 
                    if o == target:
                        #print("Save "+str([nums[a],nums[b],nums[c],nums[d]])+" equal to "+str(target)) 
                        output.append([nums[a],nums[b],nums[c],nums[d]])
                        c=c+1; 
                        d=d-1; 
                    elif o<target: 
                        c=c+1; 
                    else: 
                        d=d-1; 
                    
                    

                    

    
        return output 


            