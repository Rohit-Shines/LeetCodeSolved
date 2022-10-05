###### Flash #######
# use [a:b] to check from which place of string to which place the other strin exits
class Solution:
    def strStr(self,haystack="hellow",needle="ll"): # hello , ll
        # Base conditions
        if haystack is None or needle is None: # base condition 1
            return -1
        if haystack == needle: # base condtion 2
            return 0

        needleLength = len(needle) # needle lenght = 2 as "le"
        # Loop through the haystack and slide the window
        for i in range(len(haystack) ): #5-2+1 = 2 - needleLength+1
            if haystack[i:i + needleLength] == needle: # 0 to 2
                print("i",i)
                return
        print("-1")
        return -1

obj = Solution()
obj.strStr()