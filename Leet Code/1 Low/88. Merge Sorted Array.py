class Solution:
    def merge(self, n1=[1, 2, 3, 0, 0, 0] m= 3, n2= [2, 5, 6], n=3) -> None:
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1 ; p2 = n - 1 # seting their index
        # And move p backwards through the array, each time writing # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and n1[p1] > n2[p2]:
                n1[p] = n1[p1]
                p1 -= 1
            else:
                n1[p] = n2[p2]
                p2 -= 1

obj = Solution()
obj.merge()