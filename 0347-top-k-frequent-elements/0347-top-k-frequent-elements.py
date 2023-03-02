class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
        num_dict = sorted(num_dict, key=lambda x:num_dict.get(x))
        return [num_dict[-i] for i in range(1,k+1)]