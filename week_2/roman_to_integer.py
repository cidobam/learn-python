
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.

#Given a roman numeral, convert it to an integer.



class Solution:
    def romanToInt(self, s: str) -> int:
        values= {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
        total_value=0
        for i in range(len(s)):
            letter_value = values[s[i]]
            if i+1 < len(s) and letter_value < values[s[i+1]]:
                total_value = total_value - letter_value
            else:
                total_value = total_value + letter_value

        return total_value 
    
       
print(Solution().romanToInt("MDXC"))