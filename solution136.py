class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        frequency = {}

        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] = frequency[i] + 1

        for i in frequency:
            if frequency[i] == 1:
                return i



