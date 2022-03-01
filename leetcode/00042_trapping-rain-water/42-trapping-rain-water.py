class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_heights = [0] * length
        right_heights = [0] * length

        left_heights[0] = height[0]
        for idx, h in enumerate(height):
            if idx == 0:
                continue
            left_heights[idx] = max(h, left_heights[idx - 1])

        right_heights[-1] = height[-1]
        for idx, h in enumerate(height[::-1]):
            if idx == 0:
                continue
            right_heights[length - idx - 1] = max(h, right_heights[length - idx])

        ret = 0
        for l, r, h in zip(left_heights, right_heights, height):
            ret += min(l, r) - h

        return ret
