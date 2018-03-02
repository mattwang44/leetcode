// 1st try: Jan. 17, 2018
// https://leetcode.com/problems/hamming-distance/description/

class Solution {
public:
    int hammingDistance(int x, int y) {
        int r = x^y, count = 0;
        while(r){
            count += r&1;
            r = r>>1;
        }return count;
    }
};