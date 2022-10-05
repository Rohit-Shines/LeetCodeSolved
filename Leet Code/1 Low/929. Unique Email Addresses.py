###

class Solution:
    def numUniqueEmails(self, emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]):
        ans = {''} # why this '' is still questionable
        for email in emails:
            acc, dom = email.split("@") #acc = test.email+alex // dom = leetcode.com
            acc = acc.split("+")[0].replace(".", "") # acc testemail
            ans.add(acc + "@" + dom) # testemail@leetcode.com
        print(len(ans)-1)
        return

obj =Solution()
obj.numUniqueEmails()

