class Solution {
public:
    // time O(N), space O(N)
    // bool canJump(vector<int>& nums) {
    //     int length = nums.size();
    //     vector<bool> memo(length - 1, false); memo.push_back(true);
    //     for (int i = length - 2; i >= 0 ; i--) {
    //         for (int j = i + 1; j <= i + nums[i]; j++) {
    //             if (memo[j]) {
    //                 memo[i] = true;
    //                 break;
    //             }
    //         }
    //     }
    //     return memo[0];
    // }
    
    // time O(N), space O(1)
    bool canJump(vector<int>& nums) {
        int dest = nums.size() - 1;
        int _max = 0;
        for (int i = 0; i <= min(_max, dest); i++) {
            _max = max(_max, i + nums[i]);
        }
        return _max >= dest;
    }
};