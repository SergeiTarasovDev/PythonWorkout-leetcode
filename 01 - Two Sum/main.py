from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
        return result

exm1 = Solution()
print(exm1.twoSum([2,11,7,15], 3))

