// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/move-zeroes/description/
// try next: maintain the vector size (no erase() & insert)
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int bias = 0;
        for (int i = 0 ; i < nums.size(); i++){
            if (nums[i-bias] == 0){
                nums.erase(nums.begin()+i-bias);
                nums.insert(nums.end(),0);
                bias++;
            }
        }
    }
};