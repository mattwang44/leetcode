// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution {
public:
    bool hasAlternatingBits(int n) {
        n ^= n>>1;
        return !(n&(n+1));
    }
};

class Solution1 {
public:
    bool hasAlternatingBits(int n) {
        if (n&1) n=n>>1;
        while(n!=0){
            if ((n&3)!=2) return false;
            n=n>>2;
        }
        return true;
    }
};