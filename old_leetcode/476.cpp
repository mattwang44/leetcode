// 1st try: Jan. 26, 2018
// https://leetcode.com/problems/number-complement/description/

class Solution {
public:
    int findComplement(int num) {
        int result = 0; int count = 0;
        while(num!=0){
            result += (1-(num&1))*pow(2,count);
            num=num>>1; 
            count++;
        }
        return result;
    }
};