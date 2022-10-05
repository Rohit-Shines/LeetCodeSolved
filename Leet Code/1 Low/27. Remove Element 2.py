class Solution:
 def removeElement(self, l1=[3,2,2,3,1,2,3,3,4,5,6,8,33,2,1,3], k=3):
     l2=[]
     for i in range(len(l1)):
         if l1[i] != 3:
             l2.append(l1[i])
     print(l2)
     return


obj = Solution()
obj.removeElement()