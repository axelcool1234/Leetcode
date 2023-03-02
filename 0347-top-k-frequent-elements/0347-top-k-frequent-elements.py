class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        #Index is how much a number appears in nums, sublist contains numbers of that count index.
        num_frequency = [[] for i in range(len(nums) + 1)]
        #O(n) time, cycles through nums list and adds it to a hash map ditionary, increasing the
        #count of any repeated numbers.
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        #O(n) time, cycles through hashmap and adds all keys (numbers) to a list, with its count
        #being the index of the sublist it'll be contained in.
        for num, count in num_dict.items():
            num_frequency[count].append(num)
        #O(n) time, cycles through num_frequency backwards, adding all numbers with the highest count
        #(which is why we cycle backwards, since higher counts have higher indices).
        return_list = []
        for count in range(len(num_frequency) - 1, 0, -1):
            for num in num_frequency[count]:
                return_list.append(num)
                if len(return_list) == k:
                    return return_list