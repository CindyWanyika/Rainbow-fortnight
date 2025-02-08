class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u","A","E","I","I","O","U"]
        
        myVowels=""
        for letter in s:
            if letter in vowels:
                myVowels+=letter
        t=len(myVowels)-1
        word=""       
        for letter in s:
            if letter in vowels:
                word+=myVowels[t]
                t-=1
            else:
                word+=letter    
        return word               

            