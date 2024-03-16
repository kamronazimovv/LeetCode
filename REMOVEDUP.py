# REMOVE DUPLICATE FROM SORTED ARRAY 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_index = 1
        for l in range(1, len(nums)):
            if nums[l] != nums[l - 1]:
                nums[left_index] = nums[l]
                left_index += 1

        return left_index