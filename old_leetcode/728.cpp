// 1st try: Jan. 17, 2018
// https://leetcode.com/problems/self-dividing-numbers/description/
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result; int s; bool dsb;
        for (;left<=right;left++){
            s = left; dsb = true;
            while(s){
                if (s%10==0 || left%(s%10)!=0){dsb = false; break;}
                s/= 10;
            }
            if (dsb){result.push_back(left);}
        }
        return result;
    }
};