class Solution:
    def lengthOfLastWord(self, s="Hello World") -> int:
        p = len(s); length = 0 #
        while p > 0:
            p -= 1
            if s[p] != ' ':
                length += 1
            elif length > 0:
                print(length)
                return
        print(length)
        return

obj = Solution()
obj.lengthOfLastWord()