// 1st try: Jan. 17, 2018
// https://leetcode.com/problems/fizz-buzz/description/

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result; 
        for (int i = 1; i <= n; i++){
            if (i%3 && i%5){result.push_back(to_string(i));}
            else{
                 result.push_back((!(i%3) ? string("Fizz"):string(""))+\
                                  (!(i%5) ? string("Buzz"):string("")));
            }
        }return result;
    }
};