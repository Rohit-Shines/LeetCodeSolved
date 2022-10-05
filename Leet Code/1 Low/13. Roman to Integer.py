# add from reverse keeping last digit  in total

d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, }
class Solution:
    def romanToInt(self, s="XIII"): # IV=5-1 =4 // VI= 5+1 = 6 // so ta
        if len(s)== 0: return False # Base condition

        t = d.get(s[-1]) # pulling value from end / in this case I = 1
        for i in reversed(range(len(s) - 1)): # i =  2 , 1, 0
            print("i",i)
            # main Logic
            if d[s[i]] < d[s[i + 1]]: # if less than -
                t -= d[s[i]]
                print("t",t)
            else:
                t += d[s[i]] # if greater than or equal +

        print(t)
        return

obj=Solution()
obj.romanToInt()