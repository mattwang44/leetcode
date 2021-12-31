class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ret;
        vector<int> curr;
        helper(candidates, 0, target, curr, ret);
        return ret;
    }
private:
    void helper(vector<int>& candidates, int begin_idx, int target, vector<int>& curr, vector<vector<int>>& ret) {
        if (target == 0) {
            ret.push_back(curr);
            return;
        }
        
        for (int i = begin_idx; i < candidates.size(); i++) {
            if (candidates[i] > target) {
                return;
            }
            curr.push_back(candidates[i]);
            helper(candidates, i, target - candidates[i], curr, ret);
            curr.pop_back();
        }
        
    }
};