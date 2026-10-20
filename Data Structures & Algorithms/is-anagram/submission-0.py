'''
Valid Anagram

Pattern: Hashing

First approach:
Search and remove characters from a list.
Time: O(n²)

Optimized approach:
Count character frequencies using dictionaries.
Time: O(n)
Space: O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] +=1

        for letter in t:
            if letter not in dic2:
                dic2[letter] = 1
            else:
                dic2[letter] +=1
        
        return dic == dic2

        