class Solution:
    def maximumUnits(self, boxTypes=[[1,3],[2,2],[3,1]], truckSize=4):
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for t, u in boxTypes:
            if truckSize > t:
                truckSize -= t
                ans += t * u
            else:
                ans += truckSize * u
                print(ans)
                return ans
        print(ans)
        return ans

obj =Solution()
obj.maximumUnits()