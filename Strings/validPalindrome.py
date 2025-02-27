"""A phrase is a palindrome if, after converting all uppercase letters into
 lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
   Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new=""
        for letter in s:
            if letter.isalnum():
                new+=letter
               
        return new.lower()==new[::-1].lower()        
    
soln=Solution()
print(soln.isPalindrome("A man, a plan, a canal: Panama"))   