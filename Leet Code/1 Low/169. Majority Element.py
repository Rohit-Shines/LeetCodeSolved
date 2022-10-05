class Solution:
    def majorityElement(self, nums=[2,3,3]):
        c = 0; p = 0 # p= pointer # c= count
        for i in nums:
            if c == 0:p = i # 1st iteration
            if i == p: c += 1 # 2nd iteration
            else: c -= 1 #
        print(p)
        return

obj = Solution()
obj.majorityElement()
#
# class Solution:
#     def majorityElement(self, L1=[2,3,3]):
#         c = 0; n = None
#         for i in L1:
#             if c == 0:
#                 n = i #
#             if i == n:
#                 c +=1
#             else:
#                 -1
#             # count += (1 if num == candidate else -1)
#         print(n)
#         return
#
# obj = Solution()
# obj.majorityElement()