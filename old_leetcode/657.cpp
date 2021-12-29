// 1st try: Jan. 17, 2018
// https://leetcode.com/problems/judge-route-circle/description/
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (int i = 0; i < moves.size(); i++){
            switch(char(moves[i])){
                case 'U':
                    y++; break;
                case 'D':
                    y--; break;
                case 'R':
                    x++; break;
                case 'L':
                    x--; break;                
            }
        }
        return !x&&!y;
    }
};