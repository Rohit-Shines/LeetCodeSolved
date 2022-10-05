# wonderfull logic in single line

class Solution:
    def reverseString(self, s=["h","e","l","l","o"]):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # swapping without temp
            left, right = left + 1, right - 1  # assigning values in single line
        print(s)

obj=Solution()
obj.reverseString()