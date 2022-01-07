from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        curr_max = nums[0]
        count1 = 0
        for i in range(1, len(nums)):
            if curr_max > nums[i]:
                count1 += 1
            else:
                curr_max = nums[i]

        curr_min = nums[-1]
        count2 = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > curr_min:
                count2 += 1
            else:
                curr_min = nums[i]

        return True if count1 <= 1 or count2 <= 1 else False

print(Solution().checkPossibility([4,2,1]))