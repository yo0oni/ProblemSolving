class Solution(object):
    def removeElement(self, nums, val):
        while nums.count(val):
            nums.remove(val)
        return len(nums)