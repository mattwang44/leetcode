// 1st try: Jan. 16,2018
// https://leetcode.com/problems/number-of-1-bits/description/

class Solution {
public:
    int hammingWeight(uint32_t n) { 
        int count = 0; 
        while(n){
            count += n&1;
            n=n>>1;
        }
        return count;
    }
};