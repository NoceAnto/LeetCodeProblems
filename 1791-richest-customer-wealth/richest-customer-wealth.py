class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maximumW = 0;
        for l in accounts: 
            if maximumW < sum(l):
                maximumW = sum(l);
        
        return maximumW