class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        

        prefixsum = [0]; 
        maxaltitude = 0;
        for g in gain: 
            prefixsum.append(prefixsum[-1]+g);

            if prefixsum[-1]>maxaltitude:
                maxaltitude = prefixsum[-1];

        
        return maxaltitude