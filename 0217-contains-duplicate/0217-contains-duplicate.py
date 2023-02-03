class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_memory = set()
        for num in nums:
            if num in nums_memory:
                return True
            else:
                nums_memory.add(num)
        return False
