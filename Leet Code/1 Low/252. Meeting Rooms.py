#sort and compare 2nd value of first array to 1st values of next arrays
# understnad index print

class Solution:
    def canAttendMeetings(self, intervals=[[0,30],[15,20],[5,10]]):
        intervals.sort() #  [[0, 30], [5, 10], [15, 20]]
        for i in range(len(intervals) - 1): # direct count
            if intervals[i][1] > intervals[i + 1][0]: # 30 >5
                print("False mowa")
                return
        print("Can attend meeting")
        return

obj=Solution()
obj.canAttendMeetings()

# class Solution:
#     def canAttendMeetings(self, intervals=[[0,30],[15,20],[5,10]]):
#         intervals.sort() #  [[0, 30], [5, 10], [15, 20]]
#         print(intervals[0][0])# 0
#         print(intervals[0][1]) # 30
#         print(intervals[1][0]) #15
#         print(intervals[1][1]) # 20
#         for i in range(len(intervals) - 1): # direct count
#             if intervals[i][1] > intervals[i + 1][0]:
#                 print(intervals[i][1] ,">", intervals[i + 1][0])
#
#                 print("False mowa")
#                 return
#         print("Can attend meeting")
#         return
#
# obj=Solution()
# obj.canAttendMeetings()