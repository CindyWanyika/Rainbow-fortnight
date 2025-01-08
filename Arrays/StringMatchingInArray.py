"""Given an array of string words, return all strings in words that
 is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string"""

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        substrings=set()
        for x in words:
            for y in words:
                if x in y and x!=y:
                    substrings.add(x)
        return list(substrings)      