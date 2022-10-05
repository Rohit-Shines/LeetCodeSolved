class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        i = 0
        j = len(nums) - 1

        max_sum = -1

        while i < j:
            if nums[i] + nums[j] >= k:
                j -= 1
            else:
                max_sum = max(max_sum, nums[i] + nums[j])
                i += 1

        return max_sum
obj =Solution()
obj.twoSumLessThanK()


# class Solution:
#     def twoSumLessThanK(self, nums=[34,2,1,3,75,33,54,8], k=62):
#         top=0
#         for i in range(len(nums)-1):
#             if nums[i]>k:
#                 nums.pop(i)
#         print(nums)
#         print(max(nums))
#
#         for j in range(len(nums)-1):
#             top+=0
#             if max(nums)+nums[j]<k and max(nums)+nums[j]>top:
#                 top=max(nums)+nums[j]
#         print(top)

#
#
# obj =Solution()
# obj.twoSumLessThanK()



# class Solution:
#     def twoSumLessThanK(self, nums=[34,23,1,24,75,33,54,8], k=60):
#         answer = -1; count = [0] * 1001;  lo = 1; hi = 1000
#         for num in nums: #
#             count[num] += 1 #
#             print(count)
#
#         while lo <= hi:
#             if lo + hi >= k or count[hi] == 0:
#                 hi -= 1
#             else:
#                 if count[lo] > (0 if lo < hi else 1):
#                     answer = max(answer, lo + hi)
#                 lo += 1
#         print(answer)
#         return
#
# obj =Solution()
# obj.twoSumLessThanK()