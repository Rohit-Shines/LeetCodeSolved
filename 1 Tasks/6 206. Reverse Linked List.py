

class Solution:
    def reverseList(self, num=[1,2,3,4,5,8,9]):
        fl=len(num)-1
        for i in range(len(num)//2):
            t= num[i]
            num[i]=num[fl]
            num[fl]=t
            fl-=1
        print(num)


        #################### by using a inbuilt function ####################
        head.reverse();print(head)
        #################### #################### ####################



obj =Solution()
obj.reverseList()