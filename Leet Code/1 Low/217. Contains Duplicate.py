

def containsDuplicate(nums=[1,2,3]):
    counter = set()

    for i in nums: # 1,2,3
        if i not in counter: # if already the element exits it will not add and goes to false
            counter.add(i) # 1,2,3
        else:
            print("True")
            return
    print("False")
    return

containsDuplicate()


# this logic exceeds the time
# # using functionns
# def containsDuplicate(nums=[1,2,3,1]):
#     for i in range(len(nums)):
#         if nums.count(nums[i])>1:
#             p="true"
#             print(p)
#             return
#     print("false")
#
# containsDuplicate()

