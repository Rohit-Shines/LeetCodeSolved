#### this logic uses O(1) better logic is below
class Solution:
    def searchInsert(self, l1=[1, 3, 5, 6,7,8,9], t=9):
        for i in range(len(l1)):
            if l1[i] == t:
                print("yes this is postion",i)
                return

obj = Solution()
obj.searchInsert()


## algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, L1=[1, 3, 5, 6], t=5) -> int:
        left, right = 0, len(L1) - 1

        while left <= right:
            pivot = left + (right - left) # pivot 1,2...
            if L1[pivot] == t: # base logic
                return pivot

            if t < L1[pivot]: # 5<1
                right = pivot - 1 # 1-1 //
            else:
                left = pivot + 1
        print(left)
        return

obj = Solution()
obj.searchInsert()
#
