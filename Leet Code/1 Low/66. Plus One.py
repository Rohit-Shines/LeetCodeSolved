class Solution:
    def plusOne(self, digits=[1,2,3]):
        for i in range(len(digits)-1, -1, -1): # start stop step
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                print(digits)
                return
        print([1] + digits)
        return

obj = Solution()
obj.plusOne()