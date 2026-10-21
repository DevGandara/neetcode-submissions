'''
Two Sum

Pattern: Hashing

First approach:
Search for the indices with 2 nested loops 
Time: O(n²)

Second approach:
Store numbers as dictionary keys and their indices as lists
Search for the complement of each number, handling duplicate values when necesary
Time: 0(n) average
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if n not in dic:
                dic[n] = [i]
            else:
                dic[n].append(i)

        for n in dic.keys():
            rtarget = target - n
            if rtarget in dic and n==rtarget and len(dic[n]) >= 2:
                return[dic[n][0], dic[n][1]] 
            if rtarget in dic and n!=rtarget:
                return [dic[n][0], dic[rtarget][0]]           

        