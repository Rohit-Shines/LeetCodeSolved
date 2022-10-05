# print(increasing or decreasing) This is the main statment which prints if any of statment is true

class Solution(object):
    def isMonotonic(self, A=[1,2,3,4]):
        increasing = decreasing = True # statement o
        for i in range(len(A) - 1): # 0-3
            print(i)
            if A[i] > A[i+1]:# 3>2
                increasing = False
                print("loop1",increasing)
            if A[i] < A[i+1]:
                decreasing = False
                print("loop2",decreasing)
        print("final",increasing or decreasing)# Print anything whihc is True.
        return

obj =Solution()
obj.isMonotonic()