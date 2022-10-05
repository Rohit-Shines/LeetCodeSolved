##### Flash ##########
# stacck.append. and stack.false
# amma baboi logic // they should be in order

class Solution:
    def isValid(self, s="({)"): # they should be in order
        h = [] ; dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values(): # this is ok
                h.append(char) # (
                print("stack",h) # stack ['('] // stack ['(', '{']

            elif char in dict.keys():
                print(h.pop())
                if h == [] or dict[char] != h.pop(): # just go step by step to understand
                    #  h=[] key(}])) comes first mean false by default
                    # dict[char] != h.pop() = if theere is key } and no value { for it in dict it is false
                    print("false ra howla") # {
                    return False
            else:
                print("False ra ")
                return
        print("ok banei undi")
        return # return always used to exit the method ( definition)

obj=Solution()
obj.isValid()

# class Solution:
#     def isValid(self, s="(a{)"): # they should be in order etla paditei atla kadu
#         stack = []
#         dict = {"]":"[", "}":"{", ")":"("}
#         for char in s:
#             if char in dict.values():
#                 stack.append(char) #
#                 print("stack", stack)
#
#             elif char in dict.keys():
#                 if stack == [] or dict[char] != stack.pop():
#                     print("false anta mowa")
#                     # return False
#             else:
#                 print("ee false anta mowa")
#                 # return False
#         print("True")
#         return

