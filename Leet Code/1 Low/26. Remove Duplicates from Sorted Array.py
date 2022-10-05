class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Length of the update array
        count = 0
        # Loop for all the elements in the array
        for i in range(len(nums)):
            # If the current element is equal to the next element, we skip
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            # We will update the array in place
            nums[count] = nums[i]
            count += 1
        print(nums)
        return
obj = Solution()
obj.removeDuplicates()




#
# # method 0
# class Solution:
#     def removeDuplicates(self, l1=[1, 1, 2,3,3,4]):
#         l2=list(dict.fromkeys(l1))
#         print(l2)
#
# obj = Solution()
# obj.removeDuplicates()
#
# # method 1
# class Solution:
#     def removeDuplicates(self, l1=[1, 1, 2,3,3,4]):
#         count = 1
#         for i in range(len(l1)-1): # 0,1,2
#             # If the current element is equal to the next element, we skip
#             if l1[i] == l1[i + 1]: # 0 < (3-2) and 1 == 2
#                 continue
#             # We will update the array in place
#             l1[count] = l1[i]
#             count += 1
#         print(count)
#         print("eey",l1)
#         return
#
# obj = Solution()
# obj.removeDuplicates()
#
# # method 2
# # this is just calculating count of different variables
# # class Solution:
# #     def removeDuplicates(self, l1=[1,1,2,3,3,4,5,6,6]):
# #         count = 1;
# #         for i in range(len(l1)-1): # 0,1,2
# #             if l1[i] == l1[i+1]:
# #                 continue
# #             count += 1
# #         print(count)
# #         return
# #
# # obj = Solution()
# # obj.removeDuplicates()
