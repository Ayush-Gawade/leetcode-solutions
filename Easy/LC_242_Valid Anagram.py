"""
LeetCode 242 - Valid Anagram
Difficulty: Easy

Approach 1:
1. Use Hash maps for bpth strings s & t.
2. First check if count of Hashmap<s> == Hashmap<t>.
3. Iterate through Hashmap<s> and check occurances with Hashmap<t>

Time Complexity: O(s + t)
Space Complexity: O(s + t).....gonna need memory
"""
#Approach 1 :
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #This is for checking if there are the same no. of elements 
        countS, countT = {}, {} # created hashmaps for string s & t

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True


# Approach 2 :( using in bulit function, won't work in interviews)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        #or can use return Counter(s) == Counter(t).....[Most eff. out of these btw]

"""
Approach 3:
Time Complexity: O(s + t)
Space Complexity: O(1).....Solved memory problem
"""
#Approach 3 : here we are just gonna sort the alphabets first then compare in hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        # This approach reduces the space complexity from O(s + t) to O(1) by sorting the input strings, which reduces the need for additional data structures to store character counts.