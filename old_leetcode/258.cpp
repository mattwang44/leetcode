// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/add-digits/description/

class Solution {
public:
    int addDigits(int num) {
        if (!num) return num;
        return num%9==0?9:num%9;
    }
};