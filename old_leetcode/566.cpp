// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/reshape-the-matrix/description/

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size(), n = nums[0].size(); int len = m*n;
        if (r*c!=len) return nums;
        vector<vector<int>> result(r, vector<int>(c,0));
        for (int i = 0; i < len; i++) result[i / c][i % c] = nums[i / n][i % n];   
        return result;
    }
};
