class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] == 0:
                l += 1
            elif nums[r] == 2:
                r -= 1
            elif nums[l] == 2 or nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                _l = l
                while _l < r:
                    if nums[_l] == 1:
                        _l += 1
                    else:
                        nums[l], nums[_l] = nums[_l], nums[l]
                        break
                else:
                    break

        return nums
