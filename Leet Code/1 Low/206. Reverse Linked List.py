class Solution:
    def reverseList(self, head=[1,2,3,4,5]):
        if head == None: return None # Breaking statment
        p = head
        while p.next:
            n = p.next
            p.next = n.next
            n.next = head
            head = n

        return head
obj = Solution()
obj.reverseList()







# # Using functions
# class Solution(object):
#     def reverseList(self, nums=[1,2,3,4,5]):
#         nums.reverse()
#         print(nums)
# obj = Solution()
# obj.reverseList()