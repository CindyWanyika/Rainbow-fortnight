"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 
 """
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        listed=s.split()
        return len(listed[-1].strip())