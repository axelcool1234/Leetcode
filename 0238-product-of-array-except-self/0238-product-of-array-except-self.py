class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            answer.append(prefix)
            prefix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            answer[i] = answer[i] * postfix
            postfix *= nums[i]
        return answer
