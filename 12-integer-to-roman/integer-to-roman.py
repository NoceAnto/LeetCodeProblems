class Solution:
    def intToRoman(self, num: int) -> str:
    
        i = 0; 
        Conversion = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
        ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        ["","M","MM","MMM",".",".",".",".",".","."]];

        output = [];
        while num>0:

            digit = int(num%10); 
            print(digit)
            
            num = (num-digit)/10

            row = Conversion[i]; 
            output.append(row[digit])



            i = i + 1;

        res = ""; 
        for i in range(0,len(output)):
            res = res + output[len(output)-i-1]

        return res



                

                    

