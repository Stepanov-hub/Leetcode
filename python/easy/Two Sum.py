from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_1 = dict()

        for pos, value in enumerate(nums):
            if target - value in dict_1:
                return [dict_1[target - value], pos]
            dict_1[value] = pos

        # for pos_1 in range(len(nums)):
        #     pos_2 = dict_1.get(target - nums[pos_1], None)
        #     if pos_2 is not None and pos_1 != pos_2:
        #         return [pos_1, pos_2]
        #     dict_1[nums[pos_1]] = pos_1