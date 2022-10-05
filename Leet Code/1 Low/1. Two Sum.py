#C=n-t// dictionary value check
class Solution:
    def twoSum(self,nums=[2,7,11,15], target=9):
        HashMap = {} # Sets remove duplicates and print 1 value for 1// it is faster then list and tuples

        for i in range(len(nums)): # len of nums = 4
            HashMap[nums[i]] = i # creating {2: 0, 7: 1, 5: 2, 8:3}
            complement = target - nums[i] # 1) 7= 9-2
            if complement in HashMap: # 7 in hashmap
                return [HashMap[complement],i ] # HashMap[complement]= its like searching for the value in dictionary.
obj=Solution()
obj.twoSum()