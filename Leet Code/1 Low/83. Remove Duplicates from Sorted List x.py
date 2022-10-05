# class Solution:
#     def deleteDuplicates(self, n1=[1, 1, 2, 3]):
#         cur = n1
#         while cur:
#             if next(cur) and next(cur).val == cur.val:
#                 next(cur) = next.next(cur)
#             else:
#                 cur = cur.next
#         return n1
#
# obj = Solution()
# obj.deleteDuplicates()

# shines solution to print directly
# class Solution:
#     def deleteDuplicates(self, n= [1,1,2]):
#         print(set(n))
#
# obj = Solution()
# obj.deleteDuplicates()