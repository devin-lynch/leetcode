class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_reduced = ''
        for c in s:
            if c.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890':
                s_reduced += c
        rev_str = ''
        for i in reversed(range(len(s))):
            if s[i].lower() in 'abcdefghijklmnopqrstuvwxyz1234567890':
                rev_str += s[i]
        rev_str = rev_str.lower()
        print(s_reduced)
        print(rev_str)

        if s_reduced.lower() == rev_str:
            return True
        else:
            return False
        

print(Solution().isPalindrome('A man, a plan, a canal: Panama'))