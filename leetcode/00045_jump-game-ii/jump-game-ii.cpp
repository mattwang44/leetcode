class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) {
            return 0;
        }
        int len = nums.size();
        vector<int> memo(nums.size(), INT_MAX);
        memo[len - 1] = 0;
        for (int i = len - 2; i >= 0; i--) {
            int d = max((len - i - nums[i] - 1), 0);
            memo[i] = *min_element(memo.begin() + i+ 1, memo.end() - d) + 1;
        }
        return memo[0];
    }
};