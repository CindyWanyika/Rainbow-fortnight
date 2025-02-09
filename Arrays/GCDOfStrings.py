'''For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
 (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2)!=(str2+str1):
            return ""
        else:
            word=str1[:mygcd(len(str1),len(str2))]
            return word
    def mygcd(a,b):
        if b==0:
            return a
        else:
            mygcd(b,a%b)               
        