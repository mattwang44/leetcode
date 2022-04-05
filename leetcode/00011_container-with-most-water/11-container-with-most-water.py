class Solution:
    # time O(N), space O(1)
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            h_l = height[l]
            h_r = height[r]

            area = (r - l) * min(h_l, h_r)
            max_area = max(area, max_area)

            if h_l < h_r:
                l += 1
            else:
                r -= 1
        return max_area
