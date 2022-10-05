####### Flash#####
# Min Max

class Solution():
    def longestCommonPrefix(self, strs = ["flower","flow","flight"]):  # strs = ["flower","flow","flight"]

        if len(strs) == 0: return "" # Base Condition
        else:
            s1, s2 = max(strs), min(strs)  # S1 =flower, S2 =  flow
            i = 0 ;
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:  # string letter
                i = i + 1  # taking the count till where it matches
            print(s1[0:i])
            return

obj=Solution()
obj.longestCommonPrefix()