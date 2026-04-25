class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []

        while len(nums) != len(unique):
            for n in nums:
                if n in unique:
                    return True
                else:
                    unique.append(n)
        return False