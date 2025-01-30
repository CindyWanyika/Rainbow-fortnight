"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
 starting with word1. If a string is longer than the other, append the additional letters onto the end
   of the merged string.

Return the merged string."""
def mergeAlternately(self, word1: str, word2: str) -> str:
        size=min([len(word1),len(word2)])
        result=""
        for i in range(size):
            result+=word1[i]
            result+=word2[i]
        result+=word1[size:]
        result+=word2[size:]
        return result