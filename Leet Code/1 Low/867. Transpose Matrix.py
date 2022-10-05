
class Solution(object):
    def transpose(self, A=[[1,2,3],[4,5,6],[7,8,9]]):
        R, C = len(A), len(A[0]) # 3 rows and 3 columns // 3 lists and 3 elements in each list
        for _ in range(C):
            ans = [None] * R

        # ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val

        print(ans)
        return
        #Alternative Solution:
        #return zip(*A)


obj =Solution()
obj.transpose()
#
#
# class Solution(object):
#     def transpose(self, A=[[1,2,3],[4,5,6],[7,8,9]]):
#         R, C = len(A), len(A[0]) # 3 , 3 // 3 list each list has 3 values
#         print(R);print(C)
#
#         for _ in range(C):
#             ans= [] * R
#
#         for r, row in enumerate(A):
#             for c, val in enumerate(row):
#                 ans[c][r] = val
#
#         print(ans)
#         return
#
#         #Alternative Solution:
#         #return zip(*A)
#
# obj=Solution()
# obj.transpose()