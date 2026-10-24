class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        output = [0]*len(temperatures); 
        stack = [];        
        for i in range(1,len(temperatures)): 

            #print(stack,output)

            if temperatures[i-1]<temperatures[i]: 
                output[i-1] = 1; 

                if len(stack)!=0: 
                    N = len(stack);
                    for j in range(0,N):
                        if temperatures[stack[N-1-j]]<temperatures[i]:
                            output[stack[N-1-j]] = i-stack[N-1-j];
                            stack.pop(N-1-j)
                        else:
                            break;
            else: 
                stack.append(i-1)

            



        return output

        