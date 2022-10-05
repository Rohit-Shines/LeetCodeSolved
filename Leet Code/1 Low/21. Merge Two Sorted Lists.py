class Solution(object):
    def mergeTwoLists(self, l1=[2, 7, 8, 9], l2=[0, 1, 4, 6]):
        i=0;j=0 ;h =[] # DICTIONARY
        while i<len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                h.append(l1[i])
                i+=1
            else:
                h.append(l2[j])
                j+=1
        h = h + l1[i:] + l2[j:] # this will hellp to print left overs in the I
        print("Sorted List: " + str(h))


obj = Solution()
obj.mergeTwoLists()



# # Method works simple
#
# class Solution(object):
#     def mergeTwoLists(self, list1=[1,2,4], list2=[1,3,4]):
#         list1.extend(list2)
#         list1.sort()
#         print(list1)
#
#
# obj = Solution()
# obj.mergeTwoLists()

