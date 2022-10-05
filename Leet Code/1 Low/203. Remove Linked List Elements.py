
class Solution():
    def removeElements(self, head=[1,2,6,3,4,5,6], val=6):
        dummyHead = head(None)
        dummyHead.next = head
        node = dummyHead

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        print(dummyHead.next)
        return
obj=Solution()
obj.removeElements()





# # without using functions but pop
# def removeElements(nums=[1,2,6,6,6,3,4,5], val=2):
#     h=nums
#     for i in range(len(nums)):
#         if val==h[i]:
#             h.pop(i)
#     print("method1",h)
# removeElements()
#
#
#
# using Functions  directly
def removeElements(nums=[1,2,6,3,4,5,6], val=6):
    c=nums.count(6)
    for i in range(c):
        nums.remove(6)
    print("Method2", nums)

removeElements()
