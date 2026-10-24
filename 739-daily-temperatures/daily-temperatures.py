class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            
            # if stack is not empty and this temp is higher than last recorded temp (stack[-1])
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop() 
                answer[prev] = i - prev

            stack.append(i)

        return answer

            
        