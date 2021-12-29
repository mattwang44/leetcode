// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/ugly-number/description/

class Solution {
public:
    bool isUgly(int num) {
        if (num<=0) return 0;
        for (int i = 28; i >= 2; i--){
            if (!(i%7) || !(i%11) || !(i%13) || !(i%17) || !(i%19) || !(i%23)) continue;
            while(!(num%i)) num/=i;
        }
        return !(num-1);
    }
};