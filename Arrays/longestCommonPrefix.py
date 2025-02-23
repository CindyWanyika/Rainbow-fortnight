"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:return strs[0]
        pref=""
        word=strs[0]
        count=0

        while count<len(word):
            pref+=word[count]
            for i in strs:
                if not i.startswith(pref):
                    return pref[:-1] 
            count+=1
        return pref