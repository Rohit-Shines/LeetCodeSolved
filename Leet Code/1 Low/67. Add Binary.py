# learn binary technique below

class Solution:
    def addBinary(self, a="11", b="1"): # if 111 =1*(2^2) 1*(2^1) + 1*(2^0)
        x = int(a, 2)  # = 3 //  1*(2^1) + 0*(2^0) = 2 # use below method to understand
        y = int(b, 2)  # = 1 // 1*(2^0)
        while y:
            answer = x ^ y # Current answer without carry is XOR of x and y: answer = x^y.
            carry = (x & y) << 1 # Current carry is left-shifted AND of x and y: carry = (x & y) << 1.
            x = answer ;   y = carry
        print(bin(x)[2:]) # this wil print from 2nd digit else outpbut will be 0B100
        return
obj = Solution()
obj.addBinary()

########## Explanation for above Logic#######
# int("12", 5) = > 1 * (5 ^ 1) + 2 * (5 ^ 0) = 7
# int("0", 5) = > 0 * (5 ^ 0) = 0
# int("10", 2) = > 1 * (2 ^ 1) + 0 * (2 ^ 0) = 2


#
# binary represents a number in base 2 (0 and 1)
# octal represents a number in base 8 (0, 1, 2, 3, 4, 5, 6 and 7)
# decimal is what is used in daily (western) life to talk about integers, which is base 10 (0 through to 9).
# hexadecimal is base 16 (0 through to 9, then A, B, C, D, E, F).