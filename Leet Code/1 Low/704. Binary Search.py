# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
class Solution:
    def search(self, nums=[-1,0,3,5,9,12], target=5):
        for i in range(len(nums)):
            if nums[i]==target:
                print(i)
                return
        print("no target found")



obj=Solution()
obj.search()

# class Solution:
#     def search(self, nums=[-1,0,3,5,9,12], target=9):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             pivot = left + (right - left) // 2 #
#             if nums[pivot] == target:
#                 print(pivot)
#                 return
#             if target < nums[pivot]:
#                 right = pivot - 1
#             else:
#                 left = pivot + 1
#         print(-1)
#         return
#
# obj=Solution()
# obj.search()