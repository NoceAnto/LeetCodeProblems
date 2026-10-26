class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        
        set1 = set(nums1); 

        set2 = set(nums2); 

        setdiff12 = set1-set2;
        setdiff21 = set2-set1;        

        output = [];
        output.append(list(setdiff12))
        output.append(list(setdiff21))

        return output 