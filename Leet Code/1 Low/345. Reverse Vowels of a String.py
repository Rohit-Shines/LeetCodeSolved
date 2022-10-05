# remove all vowels and append to hash1
# Ploace none value in removed vowels spaces
# swap vowels 

class Solution:
    def reverseVowels(self, s="hello"):
        vowels = {'a', 'e', 'i', 'o', 'u'};results = []; vowels_in_s = [] # Creating hash
        for c in s: # h,e,l,l,o
            if c.lower() in vowels:  # lower will lowcase the alphabets
                vowels_in_s.append(c) # Appending the available vowels
                results.append(None) # Appending the empty value
            else:
                results.append(c)

        for i, item in enumerate(results): # creating count for value in results// 0 h  , 1 None, 2 l, 3 l,  4 None
            if not item:
                results[i] = vowels_in_s.pop() # adding the 0 value to none gap

        print("".join(results))# holle
        print("without join",results) # without join ['h', 'o', 'l', 'l', 'e']
        return

obj=Solution()
obj.reverseVowels()