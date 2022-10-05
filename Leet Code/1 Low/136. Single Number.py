# without using functions

class Solution(object):
    def singleNumber(self, nums=[3,2,2,1,1]):
        a = 0
        for i in nums:
            a ^= i # a=a^i-> xor if both inputs are different ouput is high
            print(a) # 0^11(3) = 11
        return
obj = Solution()
obj.singleNumber()


# # Using Function

class Solution:
    def singleNumber(self, nums=[2,2,1,1,44]):
        for i in nums:
            if nums.count(i) < 2:
                print(i)
                break
        return
obj = Solution()
obj.singleNumber()