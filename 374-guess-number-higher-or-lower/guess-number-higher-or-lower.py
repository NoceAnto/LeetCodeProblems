# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        high = n; 
        low = 1; 
        while True:
            #check low and high 

            #if guess(low)==0:
            #    return low 
            #if guess(high)==0:
            #    return high 

            guessed_num = low + floor((high-low)/2);
            #print(guessed_num)

            if guess(guessed_num)==1: 
                low = guessed_num+1; 
            
            elif guess(guessed_num)==-1:
                high = guessed_num-1; 
            else: 
                return guessed_num 


        