// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/power-of-two/description/
// try next time: one line bitwise operation
class Solution {
public:
    bool isPowerOfTwo(int n) {
        for (int i=31; i >= 0; i--){
            if (pow(2,i)==n) return true;
        }return false;
    }
};