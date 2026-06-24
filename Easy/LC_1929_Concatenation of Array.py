    """
    LeetCode 1929 - Concatenation of Array
    Difficulty: Easy

    Approach 1:
    1. Use Given array.
    2. Concatenate the given array with itself again.

    Approach 2:
    1. Store given array in an new empty array
    2. Repeat step 1, so it becomes concatenated

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    #Approach 1
    class Solution:
        def getConcatenation(self, nums: List[int]) -> List[int]:
            ans = []

            for i in range (2) :
                for n in nums:
                    ans.append(n)
            return ans