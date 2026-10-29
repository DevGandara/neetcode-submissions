'''
Group Anagrams

Pattern: Hashing

(No solution came up, had to watch docs to know the method)
Optimal approach:
Do an 0's array of the alphabet length, add 1 counting the frequency of each letter and add that array transformed as a tuple as key for the hash table and the other anagrams
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            
            grams[tuple(counter)].append(s)
            

        return list(grams.values())        